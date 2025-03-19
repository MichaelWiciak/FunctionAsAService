import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON received.", status_code=400)

    data = req_body.get("data")
    length = req_body.get("len")

    if not data or not length:
        return func.HttpResponse(
            "Please provide both 'data' and 'len' in the request body.", status_code=400
        )

    data_list = data.split(",")
    if len(data_list) != int(length):
        return func.HttpResponse(
            "The length of 'data' does not match 'len'.", status_code=400
        )

    try:
        sorted_data = heap_sort(list(map(int, data_list)))
    except ValueError:
        return func.HttpResponse("Data contains non-integer values.", status_code=400)

    return func.HttpResponse(f"Sorted data: {sorted_data}", status_code=200)


# query example: {"data": "5,2,3,4,1", "len": 5}


# Heap sort
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr
