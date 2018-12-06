

def bmp(weight, height, age, sex="man"):
    """
    BMR（男）=（13.7×体重（公斤））+（5.0×身高（公分））-（6.8×年龄）+66
    BMR（女）=（9.6×体重（公斤））+（1.8×身高（公分））-（4.7×年龄）+655
    :param weight: 体重 kg
    :param height: 身高 cm
    :param age: 年龄 周岁
    :param sex: 性别
    :return: BMP
    """
    if sex == "man":
        return 13.7 * weight + 5 * height - 6.8 * age + 66
    return 9.6 * weight + 1.8 * height - 4.7 * age + 655


def kcal2kj(kcal):
    """
    1大卡(kcal)=4.1858518千焦(kJ)
    :param kcal: 大卡 kcal
    :return: kj
    """
    return kcal * 4.1858518


def kj2kcal(kj):
    """

    :param kj: 千焦 kj
    :return: kcal
    """
    return kj / 4.1858518


def protein2kcal(pro):
    """

    :param pro: 蛋白质量 g
    :return: kcal
    """
    return 4 * pro


def fat2kcal(fat):
    """

    :param fat: 脂肪 g
    :return: kcal
    """
    return 9 * fat


def carbohydrate2kcal(carb):
    """

    :param carb: 碳水化合物 g
    :return: kcal
    """
    return 4 * carb


def kcal2protein(kcal):
    """

    :param kcal: 大卡 kcal
    :return: 蛋白质量 g
    """
    return kcal / 4


def kcal2fat(kcal):
    """

    :param kcal: 大卡 kcal
    :return: 脂肪 g
    """
    return kcal / 9


def kcal2carbohydrate(kcal):
    """

    :param kcal: 大卡 kcal
    :return: 碳水化合物 g
    """
    return kcal / 4


def energy_consumption(coe, bmp, ae=0):
    """

    :param coe: 运动系数
    :param bmp: 基础代谢
    :param ae: 有氧运动消耗
    :return: 每天能量消耗
    """
    return bmp * coe + ae


def fat_loss_nutrient(energy_con, reduce_energy, weight):
    """

    :param energy_con: 每天总消耗能量 kcal
    :param reduce_energy: 每天需要减少能量 kcal
    :param weight: 体重 kg
    :return: 每天蛋白质，脂肪，碳水化合物 总需求量
    """
    total_energy = energy_con - reduce_energy
    protein = 2.75 * weight
    protein_kcal = protein2kcal(protein)
    fat_kcal = total_energy * 0.2
    fat = kcal2fat(fat_kcal)
    carbohydrate_kcal = total_energy - fat_kcal - protein_kcal
    carbohydrate = kcal2carbohydrate(carbohydrate_kcal)
    return {
        "protein": (f"蛋白质:{protein:.2f}g", f"能量:{protein_kcal:.2f}kcal"),
        "fat": (f"脂肪:{fat:.2f}g", f"能量:{fat_kcal:.2f}kcal"),
        "carbohydrate": (f"碳水化合物:{carbohydrate:.2f}g", f"能量:{carbohydrate_kcal:.2f}kcal")
    }


def muscle_gain_nutrient(energy_con, increase_energy, weight):
    """

    :param energy_con: 每天总消耗能量 kcal
    :param increase_energy: 每天需要增加能量 kcal
    :param weight: 体重 kg
    :return: 每天蛋白质，脂肪，碳水化合物 总需求量
    """
    total_energy = energy_con - increase_energy
    protein = 2.2 * weight
    protein_kcal = protein2kcal(protein)
    fat_kcal = total_energy * 0.25
    fat = kcal2fat(fat_kcal)
    carbohydrate_kcal = total_energy - fat_kcal - protein_kcal
    carbohydrate = kcal2carbohydrate(carbohydrate_kcal)
    return {
        "protein": (f"蛋白质:{protein:.2f}g", f"能量:{protein_kcal:.2f}kcal"),
        "fat": (f"脂肪:{fat:.2f}g", f"能量:{fat_kcal:.2f}kcal"),
        "carbohydrate": (f"碳水化合物:{carbohydrate:.2f}g", f"能量:{carbohydrate_kcal:.2f}kcal")
    }




my_bmp = bmp(79, 184, 24)
print(f"BMP{my_bmp:.2f}kcal")
my_energy_con = energy_consumption(1.725, my_bmp, 100)
print(f"每天消耗能量{my_energy_con:.2f}kcal")
data = muscle_gain_nutrient(my_energy_con, 300, 79)
print(data)



