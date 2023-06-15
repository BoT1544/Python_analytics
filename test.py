'''
def revenue(keys: list, value: list):
    months1 = ['September', 'October', 'November', 'December']
    months2 = ['-09-', '-10-', '-11-', '-12-']
    sum_month ={}
    #for j in range(len(months1)):
        #sum_month[months1[j]] = sum(value[i] for i in range(len(value)) if months2[j] in keys[i])
    sum_month = {months1[j]: sum(value[i] for i in range(len(value)) if months2[j] in keys[i]) for j in range(len(months1))}
    #sum_month['september'] = sum(value[i] for i in range(len(value)) if '-09-' in keys[i])
    #sum_month['october'] = sum(value[i] for i in range(len(value)) if '-10-' in keys[i])
    #sum_month['november'] = sum(value[i] for i in range(len(value)) if '-11-' in keys[i])
    #sum_month['december'] = sum(value[i] for i in range(len(value)) if '-12-' in keys[i])
    return sum_month 


keys = ['2021-09-14', '2021-12-15', '2021-09-08', '2021-12-05', '2021-10-09', '2021-09-30', '2021-12-22', '2021-11-29', '2021-12-24', '2021-11-26', '2021-10-27', '2021-12-18', '2021-11-09', '2021-11-23', '2021-09-27', '2021-10-02', '2021-12-27', '2021-09-20', '2021-12-13', '2021-11-01', '2021-11-09', '2021-12-06', '2021-12-08', '2021-10-09', '2021-10-31', '2021-09-30', '2021-11-09', '2021-12-13', '2021-10-26', '2021-12-09']
value = [1270,            8413,         9028,         3703,         5739,         4095,         295,          4944,         5723,         3701,         4471,          651,         7037,          4274,        6275,          4988,        6930,          2971,        6592,         2004,          2822,         519,         3406,        2732,          5015,         2008,          316,         6333,         5700,          2887]

print(revenue(keys, value))

#months = {'september': '-09-', 'october': '-10-', 'november': '-11-', 'december': '-12-'}
'''


a = 7000000000
b = 325000000
c = b / a * 100

print(c)


