The code was written in Python.

TeldaTask.py is the program where you can manually input details from the terminal as the program runs.
TestTeldaTask.py is the program where parameters are pre-defined and the execution is in a unit test format.

I created a function called "job" which takes in parameters for the full job schedule. It takes the job function, single run expected time, scheduling frequency, a unique identifier, and the number of times that this job is supposed to occur. In this function, I logged the start and the end of each job while saving the total job execution time. This happens inside a for-loop which loops based on the number of times this job is supposed to occur. I used the "time.sleep()" function to simulate the execution and scheduling time of each job.

In the main, I made a simple while loop that takes all the desired jobs with their details sequentially until the client decides they do not want to enter any more jobs. Then I plug the "job" function with these parameters into a thread, where each thread represents a specific job, and I put the thread into an array of threads. I then start the threads and view the logs as the jobs are completed on schedule until all threads complete execution.

The unittest file is the same exact solution since I needed to reformat the code for the testing mechanism to work. I wrote three test cases and commented out the ones that were not being tested because the logs from all three tests clash and make it unreadable.

I could've started each thread whenever I took a separate job, but I instead decided to start them all at the same time for better readability while inputting the data as a client, since the logs would clash with the inputs. Also, to better display the concurrency capability of running all threads at approximately the same time.

This is the main function:

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
              " END | This job took " + str(after - before) + " to be completed!")
        totalTime = totalTime + (after - before)
        time.sleep(f4)
    print("This series of scheduled Job " + str(jt) +
          " was completed in a total of " + str(totalTime) + "s. Excluding scheduling time.")

j: job function
i1: execution time hours
i2: execution time minutes
i3: execution time seconds
n: number of times the job will occur
f1: scheduling time hours
f2: scheduling time minutes
f3: scheduling time seconds
jt: job identifier

This is how I place the inputs inside the thread:

        thread = threading.Thread(target=job, args=(
            j, h1, m1, s1, n, h2, m2, s2, jt))
        threads.append(thread)

For future improvements, I could use "schedule" import in Python to optimize the scheduling mechanism. I made it a point to not use the schedule import so I can showcase more written code. I could also optimize the organization of logging more since when the threads are running the print statements different jobs can sometimes occur in the same instance and make the logs difficult to read.
