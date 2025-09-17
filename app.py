#!/usr/bin/env python3.11
"""
Fun Fact Generator
Uses the Useless Facts API to display random fun facts
"""

import requests
import json
import time
from typing import Optional


class FunFactGenerator:
    def __init__(self):
        self.api_url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
        self.headers = {
            'User-Agent': 'FunFactGenerator/1.0 (Python 3.11)',
            'Accept': 'application/json'
        }

    def get_random_fact(self) -> Optional[str]:
        """
        Fetch a random fun fact from the API
        Returns: Fact text or None if error occurs
        """
        try:
            response = requests.get(self.api_url, headers=self.headers, timeout=10)
            response.raise_for_status()  # Raise exception for bad status codes

            data = response.json()
            return data.get('text', 'No fact text found')

        except requests.exceptions.RequestException as e:
            print(f"Error fetching fact: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON response: {e}")
            return None

    def display_fact(self, fact: str) -> None:
        """Display the fact in a formatted way"""
        if not fact:
            print("No fact to display!")
            return

        print("\n" + "=" * 60)
        print("🌟  FUN FACT GENERATOR  🌟")
        print("=" * 60)
        print(f"\n{fact}")
        print("\n" + "=" * 60)

    def run(self) -> None:
        """Main function to run the fact generator"""
        print("Welcome to the Fun Fact Generator!")
        print("Fetching a random fact for you...\n")

        while True:
            fact = self.get_random_fact()

            if fact:
                self.display_fact(fact)
            else:
                print("Failed to fetch a fact. Please try again.")

            # Ask user if they want another fact
            try:
                choice = input("\nWould you like another fact? (y/n): ").lower().strip()
                if choice not in ['y', 'yes']:
                    print("\nThanks for using the Fun Fact Generator! 👋")
                    break

                print("\nFetching another fact...")
                time.sleep(1)  # Small delay for better UX

            except KeyboardInterrupt:
                print("\n\nGoodbye! 👋")
                break


def main():
    """Main entry point"""
    generator = FunFactGenerator()

    try:
        generator.run()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Goodbye! 👋")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()