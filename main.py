import dirbuster
import scraper


def main():
    print("type help for information")
    while True:
        command = input("busterkit> ")
        command = command.split()
        if command[0] == "exit":
            break


        elif command[0] == "help":
            print("dirbuster, create a map of directories starting from a given root: dirbust <url> <wordlist> -r (get report) -o (add rescode options separated by space)")
            print("spider/scraper, scrape data from a site using a given directory map: scrape <main url> <directory map> -f filename -i (ignore robots.txt --NOT RECCOMENDED--) -o open filter options")

        elif command[0] == "dirbust":
            options = [200, 301, 302]
            #get options
            if '-r' in command:
                report = 1
            else:
                report = 0

            if '-o' in command:
                o_index = command.index('-o')
                for i in range(o_index + 1, len(command)):
                    try:
                        options.append(int(command[i]))
                    except ValueError:
                        print(f"Invalid option: {command[i]}")

            dirbuster.dirbust(command[1], f"wordlists/{command[2]}", options = options, report = report)

        elif command[0] == "scrape":
            pass

        else:
            print(f"Unknown command: {command[0]}")



if __name__ == "__main__":
    main()