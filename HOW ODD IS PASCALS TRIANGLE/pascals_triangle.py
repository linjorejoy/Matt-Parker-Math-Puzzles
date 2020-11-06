

def nthRowPascalsTriangle(n):
    term = 1
    for i in range(n + 1):
        yield (term)
        term = (term / (i + 1))*(n - i)


def writeToFile(fileName, nthRow):
    oddCount = 0
    evenCount = 0

    with open(fileName,'w') as file:
        file.write("{:^10} {:^15} {:^15}\t{:^30} {:^15} {:^15}\t{:^30}\n"
        .format("Row", "Odds(this row)", "Evens(this row)", "Odd Percentage(this row)",
         "Total Odds", "Total Evens", "Total Odds Percentage"))
        for i in range(1, nthRow + 1):
            gen = nthRowPascalsTriangle(i - 1)
            odds = 0
            evens = 0
            for num in gen:
                if(num % 2 == 0):
                    evens += 1
                else:
                    odds += 1
            oddCount += odds
            evenCount += evens
            file.write("{:>10}  {:>15} {:>15}\t{:<30} {:>15} {:>15}\t{}\n"
            .format(i, odds, evens, odds/(odds+evens), oddCount, evenCount, oddCount/(oddCount+evenCount)))
        total = oddCount + evenCount
        file.write("\n\nOdd  Percentage {:>8}".format(oddCount/total))
        file.write("\nEven Percentage {:>8}".format(evenCount/total))


writeToFile("HOW ODD IS PASCALS TRIANGLE/details_of_200_numbers.txt", 200)
