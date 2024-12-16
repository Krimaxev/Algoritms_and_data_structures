import sys
import os
import subprocess

def discover_and_run_scripts():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    task_dirs = [d for d in os.listdir(base_dir) if d.startswith('task') and os.path.isdir(os.path.join(base_dir, d))]

    for task_dir in task_dirs:
        src_dir = os.path.join(base_dir, task_dir, 'src')

        if not os.path.exists(src_dir):
            continue

        scripts = [f for f in os.listdir(src_dir) if f.endswith('.py')]

        for script in scripts:
            script_path = os.path.join(src_dir, script)

            try:
                result = subprocess.run(
                    [sys.executable, script_path],
                    cwd=src_dir,
                    capture_output=True,
                    text=True
                )

                if result.stdout:
                    print(result.stdout)
                if result.stderr:
                    print(f"Ошибки:\n{result.stderr}")

            except Exception as e:
                print(f"Ошибка при запуске {script} из {task_dir}/src: {e}")

if __name__ == "__main__":
    discover_and_run_scripts()