import wikipedia
# from wikipedia import DisambiguationError

while True:
    topic = input("Enter page title: ")
    if not topic:
        break

    try:
        page = wikipedia.page(topic)

        print(page.title)
        print(page.summary)
        print(page.url, "\n")

    except wikipedia.exceptions.PageError:
        print(f'Page id "{topic}" does not match any pages. Try another id!\n')

    except wikipedia.exceptions.DisambiguationError:
        print(f"We need more specific title. Try one of the following, or a new search:")
        print(wikipedia.search(topic), "\n")
print("Thank you.")
