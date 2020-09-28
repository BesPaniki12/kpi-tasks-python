# расчет kpi:
# # Хомворк
fail = open("C:/Users/Home-1/Desktop/homework.txt")
bs_hw = int(5000) # базовая ставка 5к для хв
plm_hw = int(405) # план на текущий месяц
zaf_hw = int(fail.read()) # сколько получилось
procp_hw = int(bs_hw * 10 / 100)# добавочный 10% от базовой ставки
c_hw = zaf_hw-plm_hw # разница заявок между фактом и планом
aa_hw = float('{:.1f}'.format(c_hw/plm_hw*100)) # на сколько процентов заявок больше чем в kpi
if zaf_hw<plm_hw:
    print("план не выполнен")
elif zaf_hw==plm_hw:
    print(bs_hw)
elif zaf_hw>plm_hw:
    print("премия хв:", int(bs_hw+(procp_hw*aa_hw)), "руб.")

# # Диссертатус
failq = open("C:/Users/Home-1/Desktop/dissertat.txt")

bst_ds = int(3000) # базовая ставка 3к для дисс
pl_m_ds = int(70) # план на текущий месяц
zayavok_po_faktu_ds = int(failq.read()) # сколько получилось
c_ds = zayavok_po_faktu_ds-pl_m_ds # разница заявок между фактом и планом
aa_ds = float('{:.1f}'.format(c_ds/pl_m_ds*100)) # на сколько процентов заявок больше чем в kpi
if zayavok_po_faktu_ds<pl_m_ds:
    print("план не выполнен")
elif zayavok_po_faktu_ds==pl_m_ds:
    print("премия дисс:",bst_ds)
elif zayavok_po_faktu_ds>pl_m_ds:
    if 0 <= aa_ds < 5:  # равно 0 или меньше 105
        proc_pr_ds = 0
    if 5 <= aa_ds < 20:  # если больше 105-119 процентов
        proc_pr_ds = int(bst_ds * 1.1)
    elif 20 <= aa_ds < 50:  # если больше 120-149 процентов
        proc_pr_ds = int(bst_ds * 1.3)
    elif aa_ds >= 50:  # если больше 150 процентов
        proc_pr_ds = int(bst_ds * 2)
    print("премия дисс:", int(bst_ds+proc_pr_ds), "руб.")





