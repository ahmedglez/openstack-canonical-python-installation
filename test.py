import subprocess;
import time
timeout = time.time() + 60*5   # 5 minutes from now
output = subprocess.run(["echo", "prueba"]);
while (timeout > 0 & output.returncode != 0):
    test = 0
    print(output.returncode);
    print(timeout);
    if test == 5 or time.time() > timeout:
        subprocess.run(["echo", "error"])
        break
    test = test - 1;

