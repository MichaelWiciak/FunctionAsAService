# FunctionAsAService

https://docs.openfaas.com/tutorials/first-python-function/

Microsoft Azure Functions

and

OpenFaas.

Need to do a literature review of these and paper.
Karim paper is about oversource OpenFaas
now need a papaer about Microsoft Azure Functions

Sorting a list with a lambda function
but computationally hard problems
Give list generate etc.

Python always gives problems so next try with Java.

Ideas for performance: of course what they already measure in the portal, but also would be nice to record the latency since sending it locally and it getting to the cloud and back is a big part of the latency. Also, the time it takes to start the function. warm and cold starts can be checked and assessed.

Cool, so once i got both working, I want to design a script that will send request in specific orders/times, record the output data locally and use the monitoring tools to see some metrics.

Ideas: Cold Start vs. Warm Start Performance

Concurrency & Scalability Test
What? Measure how the platform handles multiple simultaneous function invocations (e.g., 10, 100, 1000 requests).
Why? Some platforms scale better, while others introduce bottlenecks.
How? Use a load-testing tool (e.g., Apache JMeter, Locust, Artillery) to fire many requests at once. Measure response time and success rate.

explain : motivation behind choice of function and platform,

After deploying the functions on the created resources for Azure and the open source serverless platform, e.g. OpenFaaS, their performance would be measured using Apache JMeter [https://jmeter.apache.org/index.html]. It is an open-source tool that enables the user to easily stress test Web applications as it can use concurrent processes to send requests, capture data and plot it according to user settings. so use jmeter.

Problem motivation: explain why you're doing this coursework. what problem are you addressing? why is it important that you address it?

heap sort shouild be nlogn when scalling, check that for both that is the case or there is overhead.

Answers:

Q1)

Commercial serverless platform:
Microsoft Azure Functions
Open-source serverless platform:
OpenFaaS
Programming Language:
Python
Application description:
Heap Sort of a unordered list of integers, looking at how the platforms handle large payloads of data.

References:
Wiredu, Japheth & Aabaah, Iven & Wiredu, Reuben. (2024). Optimizing Heap Sort for Repeated Values: A Modified Approach to Improve Efficiency in Duplicate-Heavy Data Sets. International Journal of Advanced Research in Computer Science. 15. 12-18. 10.26483/ijarcs.v15i6.7152.

Q2)
This coursework examines how FaaS platforms handle computationally intensive tasks like Heap Sort, which plays a key role in Big Data analytics (Wiredu et al., 2024). The problem being addressed is the challenge of efficiently executing sorting operations at scale, particularly when performed continuously. Since Heap Sort has a predictable \(O(n \log n)\) complexity, it provides a stable benchmark for evaluating platform scalability.

This is important because organisations increasingly rely on cloud computing for large-scale data processing, and Python—the dominant language in data science—is the likely choice for such tasks. Understanding the performance trade-offs of executing Heap Sort in FaaS environments will provide valuable insights into their suitability for real-world applications.

Intergrate:
An in-place, non-stable algorithm with a guaranteed O(n log n) time complexity, making it efficient for large datasets.

Related work:
...

Q3)

Q4)
