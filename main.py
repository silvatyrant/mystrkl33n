import click
import enchant
import sys

@click.command()
@click.argument('wordlist', type=click.File('r'))
@click.option('-d', '--remove-duplicates', is_flag=True, help='Remove duplicate words')
@click.option('-b', '--blacklist', type=click.File('r'), help='Path to the blacklist file')
@click.option('-o', '--output', type=click.Path(), help='Output file path')
@click.option('-e', '--english-check', type=str, help='Comma-separated list of dictionaries for English word check')
@click.option('-c', '--case-insensitive', is_flag=True, help='Perform case-insensitive checks')
@click.option('-s', '--show-stats', is_flag=True, help='Show stats')
def process_wordlist(wordlist, remove_duplicates, blacklist, output, english_check, case_insensitive, show_stats):
    # Read the word list file
    words = wordlist.read().splitlines()

    # Remove duplicates if the flag is provided
    original_word_count = len(words)
    deduped_word_count = len(set(words))
    if remove_duplicates:
        words = list(set(words))

    # Remove words from the blacklist if provided
    original_blacklist_size = 0
    if blacklist:
        blacklist_words = blacklist.read().splitlines()
        original_blacklist_size = len(blacklist_words)
        if case_insensitive:
            blacklist_words = [word.lower() for word in blacklist_words]
        words = [word for word in words if word not in blacklist_words]

    # Perform English word check and add to blacklist if required
    if english_check:
        english_dictionaries = english_check.split(',')
        for dictionary_name in english_dictionaries:
            d = enchant.Dict(dictionary_name)
            if case_insensitive:
                words = [word for word in words if not d.check(word.lower())]
            else:
                words = [word for word in words if not d.check(word)]


    # Print the resulting word list to stdout or write it to a file
    if output:
        with open(output, 'w') as output_file:
            for word in words:
                output_file.write(word + '\n')
    else:
        for word in words:
            print(word)


    if show_stats:
        print("\nStatistics:")

        # Calculate percentage reduction
        percentage_reduction = calculate_percentage_reduction(original_word_count, deduped_word_count)

        # Create progress bar
        progress_bar_length = 30
        filled_length = int(progress_bar_length * percentage_reduction / 100)
        remaining_length = progress_bar_length - filled_length

        # Define progress bar colors
        filled_color = '\u001b[41m'  # Red background
        remaining_color = '\u001b[42m'  # Green background
        end_color = '\u001b[0m'  # Reset color

        # Build progress bar string
        progress_bar = filled_color + '█' * filled_length + remaining_color + '█' * remaining_length + end_color

        # Print progress bar
        print(f"Progress: [{progress_bar}] {percentage_reduction}%")

        # Print other stats
        print(f"Original word count: {original_word_count}")
        print(f"Deduped word count: {deduped_word_count}")
        print(f"Words removed: {original_word_count - len(words)}")
        print(f"Original blacklist size: {original_blacklist_size}")
        print(f"Modified blacklist size: {original_blacklist_size - len(blacklist_words)}")

def show_banner():
    banner_path = 'banner'
    try:
        with open(banner_path, 'r', encoding='utf-8') as banner_file:
            banner_content = banner_file.read()
            print(banner_content)
    except FileNotFoundError:
        pass

def calculate_percentage_reduction(original_count, new_count):
    if original_count == 0:
        return 0
    return round(((original_count - new_count) / original_count) * 100, 2)

if __name__ == '__main__':
    show_banner()
    process_wordlist()

