from django.shortcuts import render
import os
import subprocess, tempfile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def run_code(request):
    try:
        lang = request.POST.get("lang")
        code = request.POST.get("code")


        shared_dir = "/shared"
        os.makedirs(shared_dir, exist_ok=True)

        suffix_map = {"python": ".py", "cpp": ".cpp", "js": ".js"}
        suffix = suffix_map[lang]

        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix, dir=shared_dir) as f:
            f.write(code.encode())
            filename = f.name  

        commands = {
            "python": ["docker", "exec", "docker_python", "python3", filename],
            "cpp": ["docker", "exec", "docker_cpp", "bash", "-c", f"g++ {filename} -o /shared/a.out && /shared/a.out"],
            "js": ["docker", "exec", "docker_js", "node", filename],
        }

        result = subprocess.run(commands[lang], capture_output=True, text=True, timeout=1)
        stdout_clean = result.stdout.strip()
        return JsonResponse({"stdout": stdout_clean, "stderr": result.stderr})
    except subprocess.TimeoutExpired:
        return JsonResponse({
            "error": "timeout",
            "stderr": "Execution took too long (possibly infinite loop)"
        }, status=408)

    except Exception as e:
        return JsonResponse({
            "error": str(e)
        }, status=500)