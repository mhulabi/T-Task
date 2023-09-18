import time
import threading

# To keep track of all the threads started
threads = []


def job(j, i1, i2, i3, n, f1, f2, f3, jt):
    totalTime = 0.0
    i4 = (i1*60*60) + (i2*60) + i3
    f4 = (f1*60*60) + (f2*60) + f3
    for k in range(n):
        print("Job " + str(jt) + "-" + str(k+1) + ": " + j + " START")
        before = time.perf_counter()
        time.sleep(i4)
        after = time.perf_counter()
        print("Job " + str(jt) + "-" + str(k+1) + ": " + j +
              " END | This job took " + str(round((after - before), 2)) + " to be completed!")
        totalTime = totalTime + (after - before)
        time.sleep(f4)

    print("This series of scheduled Job " + str(jt) +
          " was completed in a total of " + str(round(totalTime, 2)) + "s. Excluding scheduling time.")


if __name__ == "__main__":
    print("Welcome to job scheduling!")
    t = ""
    # Part of the unique job identifier
    jt = 1
    while t != 'no':
        j = input("Please specify the job: ")
        i = input(
            "Please specify the amount of time the job should take in the format of hh:mm:ss ")
        n = int(input(
            "Please specify how many times you wish for this job to be executed: "))
        f = input(
            "Please specify how much time there should be in between each job execution in the format of hh:mm:ss ")

        h1 = int(i[0:2])
        m1 = int(i[3:5])
        s1 = int(i[6:8])
        h2 = int(f[0:2])
        m2 = int(f[3:5])
        s2 = int(f[6:8])

        # Create a new thread
        thread = threading.Thread(target=job, args=(
            j, h1, m1, s1, n, h2, m2, s2, jt))
        threads.append(thread)

        # Possibility to create a new job if desired
        t = input(
            "Are there anymore jobs you would like to schedule? \nPlease enter yes or no: ")
        jt = jt + 1

    # for logging to be clear we take all potential jobs first then we run them concurrently
    for thh in threads:
        thh.start()

    for th in threads:
        th.join()

    print("End of all job scheduling processes!")
