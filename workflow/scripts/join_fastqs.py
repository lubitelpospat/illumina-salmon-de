import subprocess

def join_fastqs(fastqs:list, target_fp:str):
     command_str = f"zcat -f -- {' '.join(list(map(lambda x: x + '/*/fastq_pass/*', fastqs)))} > {target_fp}"
     try:
          shell_res = subprocess.run(command_str, shell=True,check=True, capture_output=True) # will raise a CalledProcessError if command will return non-zero status code
     except Exception as e:
          print(shell_res)
          raise e

join_fastqs(snakemake.input, snakemake.output)