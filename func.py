import cProfile
import pstats
import time

def do_stuff():
     
    # single line to find factorial
    result = []
    for i in range(100000):
        result.append(i ** 2)
    return result    


if __name__ == "__main__":
    with cProfile.Profile() as profile:
        start = time.time()
        print("Cameron:", do_stuff())
        end = time.time()
        print(end - start)

    results = pstats.Stats(profile)
    results.sort_stats(pstats.SortKey.TIME)
    results.print_stats()


