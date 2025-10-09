# from django.shortcuts import render
# import os
# import subprocess, tempfile
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def run_code(request):
#     try:
#         lang = request.POST.get("lang")
#         code = request.POST.get("code", "")
#         # value = request.POST.get('var',"")
#         value = "1\n2\n"


#         shared_dir = "/shared"
#         os.makedirs(shared_dir, exist_ok=True)

#         suffix_map = {"python": ".py", "cpp": ".cpp", "js": ".js"}
#         suffix = suffix_map.get(lang)
#         if not suffix:
#             return JsonResponse({"error": "Unsupported language"}, status=400)

#         with tempfile.NamedTemporaryFile(delete=False, suffix=suffix, dir=shared_dir) as f:
#             f.write(code.encode())
#             filename = f.name

#         commands = {
#             "python": ["docker", "exec","-i", "docker_python", "python3", filename],
#             "cpp": ["docker", "exec","-i", "docker_cpp", "bash", "-c", f"g++ {filename} -o /shared/a.out && /shared/a.out"],
#             "js": ["docker", "exec","-i", "docker_js", "node", filename],
#         }

#         process = subprocess.Popen(
#             commands[lang],
#             stdin=subprocess.PIPE,
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE,
#             text=True
#         )

#         try:
#             stdout, stderr = process.communicate(input=value + "\n", timeout=1)
#         except subprocess.TimeoutExpired:
#             process.kill()
#             stdout, stderr = "", "Time limit exceeded"

#         stdout_clean = stdout.strip()
#         stderr_clean = stderr.strip()

#         return JsonResponse({
#             "stdout": stdout_clean,
#             "stderr": stderr_clean
#         })

#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=500)

from rest_framework import routers, serializers, viewsets

class UserViewSet(viewsets.ModelViewSet):
    pass