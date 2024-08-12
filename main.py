def count_words(path):
  return len(get_text(path).split())

def count_chars(path):
  text = get_text(path).lower()
  counts = {}
  for c in text:
    if c in counts:
      counts[c] += 1
    else:
      counts[c] = 1
  return counts

def print_text(path):
  print(get_text(path))

def get_text(path):
  with open(path) as f:
    return f.read()

def make_report(counts):
  report = []
  for c in counts:
    if c.isalpha():
      report.append({ "name": c, "count": counts[c] })
  report.sort(reverse=True, key=lambda x: x["count"])
  for l in report:
    print(f"The '{l['name']}' character was found {l['count']} times")

def main(path):
  d = count_chars(path)
  make_report(d)

book_path = 'books/frankenstein.txt'
main(book_path)
