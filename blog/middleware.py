import time

def request_time_middleware(get_response):
    def middleware(request):
        start_time = time.time()

        response = get_response(request)

        end_time = time.time()
        duration = end_time - start_time

        print(f"Request to {request.path} took {duration:.4f} seconds")

        return response

    return middleware
