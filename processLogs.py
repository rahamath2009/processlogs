import sys
import os
import datetime

timeDelta = {}

def processLogs(filePath):
	td = datetime.datetime.now()
	if os.path.exists(filePath):
		with open('samplelog.txt') as fp:
			rows = fp.readlines()
			for rec in rows:
				info = rec.split(' ')
				tm = info[0].split(':')
				if 'start' in rec:
					if info[1] not in timeDelta:
						timeDelta[info[1]] = {
						'status': 'Active',
						'st_time': datetime.datetime(
							td.year, td.month, td.day,\
							int(tm[0]), int(tm[1]), int(tm[2])
							),
						'total_seconds': 0
						}
					else:
						timeDelta[info[1]]['st_time'] = datetime.datetime(
							td.year, td.month, td.day,\
							int(tm[0]), int(tm[1]), int(tm[2])
							)
				else:
					if info[1] not in timeDelta:
						timeinfo  = datetime.datetime(
							td.year, td.month, td.day,\
							int(tm[0]), int(tm[1]), int(tm[2])
							)

						timeDelta[info[1]] = {
						'status': 'Inactive',
						'end_time': datetime.datetime(
							td.year, td.month, td.day,\
							int(tm[0]), int(tm[1]), int(tm[2])
							),
						'total_seconds': 0
						}
					else:
						timeDelta[info[1]]['end_time'] = 0
						try:
							timeDelta[info[1]]['total_seconds'] = (timeinfo - timeDelta[info[1]]['st_time']
								).total_seconds()
						except:
							row1 = rows[0].split()
							tm = info[0].split(':')
							try:
								st_time  = datetime.datetime(
								td.year, td.month, td.day,\
								int(tm[0]), int(tm[1]), int(tm[2])
								)
								timeDelta[info[1]]['total_seconds'] += (timeinfo - st_time).total_seconds()
							except:
								continue


	return timeDelta

filePath = str(sys.argv[1])
print(processLogs(filePath))