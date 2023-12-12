def part1():
  sum = 0

  with open('input.txt') as file:
    for line in file:
      first = 0
      last = 0
      for character in line.rstrip():
        if character.isdigit():
          last = character
      for character in line.rstrip()[::-1]:
        if character.isdigit():
          first = character
      sum += int(first + last)
  print("Part1: %i\n" % (sum))

part1()