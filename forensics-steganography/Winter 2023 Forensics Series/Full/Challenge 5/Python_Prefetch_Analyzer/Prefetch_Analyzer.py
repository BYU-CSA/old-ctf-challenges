# This is a modification of a beautiful project that was discontinued some 4-8 years ago. So I'm altering it and giving it to you.

import pyscca
pyscca.get_version()
scca = pyscca.file()
scca.open(<path to prefetch file>)

last_run_times = []
for x in range(8): # Prefetch only stores 8 last run times
    if scca.get_last_run_time_as_integer(x) > 0:
        last_run_times.append(scca.get_last_run_time(x).strftime("%Y-%m-%d %H:%M:%S")) #str conversion utilized to change from datetime into human-readable
    else:
        last_run_times.append('N/A')
print('Last run times:')
print(last_run_times)

file_names = []
end_of_file = False
x = 0
while not end_of_file:
    try:
        file_names.append(scca.get_filename(x))
        x += 1
    except Exception as e:
        end_of_file = True

for file_name in file_names:
    print(file_name)