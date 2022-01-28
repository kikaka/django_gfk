from time import perf_counter


class PerfCountMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        print("Init Perf Count Middleware")
        print("get response", self.get_response)

    def __call__(self, request):
        #print("__call__ vor response")
        #print("Request: ", request)

        start = perf_counter()
        response = self.get_response(request)
        end = perf_counter()
        print(f"Die Operation hat {end - start:.2f} Sekunden gedauert")
        #print("__call__ nach response")
        #print("Response: ", response)
        return response
