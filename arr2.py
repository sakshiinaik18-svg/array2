def main():
    scores=[78,99,86,66,52]
    total=sum(scores)
    average=total/len(scores)
    print("== main/master branch output ==")
    print(f"score: {scores}")
    print(f"total: {total}")
    print(f"average: {average}")
    print("== local branch output ==")
    print(f"Maximum={max(scores)}")
    print(f"Minimum={min(scores)}")
if __name__ == "__main__":
    main()
