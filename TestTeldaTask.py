import time
import threading
import unittest


def aquire(threads):
    print("Welcome to job scheduling!")

    # for logging to be clear we take all potential jobs first then we run them concurrently
    for thh in threads:
        thh.start()

    for th in threads:
        th.join()

    print("End of all job scheduling processes!")

    return 0


def job(j, i1, i2, i3, n, f1, f2, f3, jt):
    totalTime = 0.0
    i4 = (i1*60*60) + (i2*60) + i3
    f4 = (f1*60*60) + (f2*60) + f3
    print("Each individual job is in process for a total of " + str(i4) + "s")
    print("The scheduling time in between each job is " + str(f4) + "s")
    for k in range(n):
        print("Job " + str(jt) + "-" + str(k+1) + ": " + j + " START")
        before = time.perf_counter()
        time.sleep(i4)
        after = time.perf_counter()
        print("Job " + str(jt) + "-" + str(k+1) + ": " + j +
              " END | This job took " + str(round((after - before), 2)) + "s to be completed!")
        totalTime = totalTime + (after - before)
        time.sleep(f4)

    print("This series of scheduled Job " + str(jt) +
          " was completed in a total of " + str(round(totalTime, 2)) + "s. Excluding scheduling time.")

# Class made for testing


class Ttest(unittest.TestCase):
    """
    # Two different concurrent jobs
    def test_function_1(self):
        test_thread_1 = []
        thread1 = threading.Thread(target=job, args=(
            "Billing", 0, 2, 0, 3, 0, 0, 10, 1))
        test_thread_1.append(thread1)

        thread2 = threading.Thread(target=job, args=(
            "Gardening", 0, 4, 0, 2, 0, 0, 5, 2))
        test_thread_1.append(thread1)

        result = aquire(test_thread_1)

        self.assertAlmostEqual(result, 0)

    """
    # Four different concurrent jobs

    def test_function_2(self):
        test_thread_2 = []
        thread1 = threading.Thread(target=job, args=(
            "Billing", 0, 2, 0, 3, 0, 0, 10, 1))
        test_thread_2.append(thread1)

        thread2 = threading.Thread(target=job, args=(
            "Gardening", 0, 4, 0, 2, 0, 0, 5, 2))
        test_thread_2.append(thread2)

        thread3 = threading.Thread(target=job, args=(
            "Programming", 0, 5, 0, 1, 0, 0, 0, 3))
        test_thread_2.append(thread3)

        thread4 = threading.Thread(target=job, args=(
            "Management", 0, 0, 30, 3, 0, 1, 30, 4))
        test_thread_2.append(thread4)

        result = aquire(test_thread_2)

        self.assertAlmostEqual(result, 0)
    """
    # Two identical concurrent jobs, only the job-detail and identifier are different
    def test_function_3(self):
        test_thread_3 = []
        thread1 = threading.Thread(target=job, args=(
            "Billing", 0, 2, 0, 3, 0, 0, 10, 1))
        test_thread_3.append(thread1)

        thread2 = threading.Thread(target=job, args=(
            "Gardening", 0, 2, 0, 3, 0, 0, 10, 2))
        test_thread_3.append(thread1)

        result = aquire(test_thread_3)

        self.assertAlmostEqual(result, 0)
        """


if __name__ == "__main__":
    unittest.main()
