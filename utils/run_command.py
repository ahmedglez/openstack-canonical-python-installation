import subprocess
import sys

def _run(command, env=None, check=False, timeout=None):
    with subprocess.Popen(args=command, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) as process:
        for line in iter(process.stdout.readline,''):
            if(line!=''):
                print (line)
        try:
            stdout, stderr = process.communicate(input, timeout=timeout)
        except subprocess.TimeoutExpired:
            process.kill()
            stdout, stderr = process.communicate()
            raise subprocess.TimeoutExpired(
                process.args, timeout, output=stdout, stderr=stderr,
            )
        except Exception:
            process.kill()
            process.wait()
            raise
        retcode = process.poll()
        if check and retcode:
            raise subprocess.CalledProcessError(
                retcode, process.args, output=stdout, stderr=stderr,
            )
        return subprocess.CompletedProcess(process.args, retcode, stdout, stderr)