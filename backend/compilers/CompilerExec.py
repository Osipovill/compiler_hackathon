import subprocess
import tempfile

class Compiler:
    def compile_cpp(self, code: str) -> str:
        with tempfile.NamedTemporaryFile(suffix=".cpp", delete=False, mode='w') as src:
            src.write(code)
            src.flush()
            try:
                # Компилируем C++ код
                compile_result = subprocess.run(["g++", src.name, "-o", src.name + ".exe"], capture_output=True, text=True)
                if compile_result.returncode != 0:
                    return compile_result.stderr

                # Запускаем скомпилированную программу
                run_result = subprocess.run([src.name + ".exe"], capture_output=True, text=True)
                return run_result.stdout if run_result.returncode == 0 else run_result.stderr
            finally:
                subprocess.run(["rm", src.name + ".exe", src.name])  # Очистка

    def compile_java(self, code: str) -> str:
        with tempfile.NamedTemporaryFile(suffix=".java", delete=False, mode='w') as src:
            src.write(code)
            src.flush()
            try:
                # Компилируем Java код
                compile_result = subprocess.run(["javac", src.name], capture_output=True, text=True)
                if compile_result.returncode != 0:
                    return compile_result.stderr

                # Запускаем Java класс
                run_result = subprocess.run(["java", "-cp", tempfile.gettempdir(), "Temp"], capture_output=True, text=True)
                return run_result.stdout if run_result.returncode == 0 else run_result.stderr
            finally:
                subprocess.run(["rm", src.name])  # Очистка

    def compile_python(self, code: str) -> str:
        with tempfile.NamedTemporaryFile(suffix=".py", delete=False, mode='w') as src:
            src.write(code)
            src.flush()
            # Запускаем Python скрипт
            run_result = subprocess.run(["python", src.name], capture_output=True, text=True)
            return run_result.stdout if run_result.returncode == 0 else run_result.stderr
        def compile_js(self, code: str) -> str:
                with tempfile.NamedTemporaryFile(suffix=".js", delete=False, mode='w') as src:
                        src.write(code)
                        src.flush()
                        # Запускаем JavaScript файл
                        run_result = subprocess.run(["node", src.name], capture_output=True, text=True)
                        return run_result.stdout if run_result.returncode == 0 else run_result.stderr
        def sort(self, type:str, code:str) -> str:
                if type == "python":
                        return self.compile_python(code)
                elif type == "java":
                        return self.compile_java(code)
                elif type == "cpp":
                        return self.compile_cpp(code)
                elif type == "js":
                        return self.compile_js(code)
                else:
                        return "Unsupported language"
