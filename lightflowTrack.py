__author__ = 'Allan'
import cv2
import numpy as np
import globalSetting as gs
import time
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-o","--out_path",help=("this is a video output path"))
ap.add_argument("-l1","--img1",help=("logo1"))
ap.add_argument("-l2","--img2",help=("logo2"))
args = vars(ap.parse_args())

position_center_a = [201.00024, 200.9494, 200.92194, 200.90083, 200.91452, 200.92242, 200.92569, 200.92853, 200.94217, 200.96042, 200.97974, 200.99808, 201.01086, 201.01523, 201.02448, 201.02963, 201.02304, 201.01724, 201.01465, 201.01239, 201.0098, 201.00803, 201.00735, 201.00587, 201.0224, 201.05112, 201.05089, 201.04718, 201.0477, 201.04514, 201.05043, 201.05763, 201.06979, 201.07407, 201.07861, 201.07635, 201.06622, 201.0119, 200.94678, 200.8956, 200.85849, 201.1799, 201.28152, 201.04672, 201.05461, 201.07977, 201.10406, 201.11465, 201.13666, 201.15315, 201.17705, 201.1985, 201.21912, 201.22144, 201.22362, 201.22278, 201.22272, 201.22281, 201.22006, 201.21872, 201.21741, 201.20154, 201.20032, 201.20847, 201.20866, 201.20706, 201.19562, 201.18909, 201.18683, 201.18222, 201.18839, 201.18552, 201.18433, 201.17825, 201.17365, 201.15906, 201.1424, 201.14084, 201.1391, 201.13293, 201.1333, 201.12939, 201.12401, 201.12671, 201.12671, 201.12996, 201.13405, 201.13974, 201.14809, 201.15439, 201.16666, 201.18536, 201.19455, 201.20763, 201.2282, 201.23561, 201.24843, 201.25809, 201.26447, 201.2681, 201.26907, 201.26678, 201.26619, 201.26013, 201.25735, 201.2572, 201.25456, 201.24286, 201.23459, 201.21936, 201.21176, 201.20387, 201.19162, 201.19302, 201.16837, 201.14996, 201.14735, 201.12125, 201.0947, 201.10822, 201.12341, 201.13147, 201.13281, 201.13414, 201.13643, 201.13632, 201.13965, 201.14252, 201.1355, 201.1315, 201.1228, 201.12726, 201.13248, 201.13159, 201.13585, 201.15839, 201.1935, 201.19714, 201.19891, 201.21436, 201.23662, 201.24063, 201.23779, 201.23463, 201.21213, 201.18658, 201.16724, 201.16776, 201.16553, 201.16731, 201.16953, 201.18378, 201.19667, 201.2189, 201.2467, 201.27191, 201.29843, 201.32825, 201.33037, 201.33244, 201.32988, 201.32782, 201.32391, 201.30319, 201.30862, 201.31506, 201.32239, 201.32552, 201.32939, 201.33511, 201.33769, 201.34575, 201.35153, 201.35721, 201.36105, 201.36136, 201.36078, 201.35913, 201.35722, 201.35809, 201.36009, 201.37064, 201.37857, 201.38986, 201.40939, 201.42075, 201.44095, 201.46881, 201.48326, 201.50381, 201.53497, 201.54738, 201.56567, 201.59224, 201.71486, 201.4855, 201.38205, 201.91949, 202.0016, 202.03323, 202.06885, 202.08984, 202.10049, 202.10797, 202.12836, 202.13295, 202.13599, 202.13757, 202.17859, 202.19279, 202.17169, 202.1467, 202.14447, 202.1436, 202.15158, 202.15076, 202.1568, 202.16177, 202.16052, 202.15977, 202.15215, 202.14417, 202.14359, 202.13998, 202.12067, 202.11774, 202.10213, 202.08928, 202.0737, 202.06889, 202.06462, 202.0603, 202.0564, 202.05774, 202.05894, 202.05711, 202.05693, 202.06732, 202.0771, 202.07919, 202.08867, 202.10757, 202.10962, 202.11862, 202.11925, 202.11993, 202.11911, 202.11987, 202.11987, 202.11421, 202.11426, 202.1142, 202.11429, 202.11423, 202.11517, 202.11609, 202.11703, 202.11847, 202.11154, 202.10712, 202.10327, 202.09851, 202.09166, 202.09677, 202.10132, 202.10916, 202.11264, 202.12064, 202.12329, 202.12772, 202.12775, 202.12616, 202.1257, 202.1236, 202.12204, 202.12537, 202.12785, 202.13081, 202.13156, 202.13905, 202.14325, 202.14957, 202.15012, 202.15181, 202.15271, 202.16254, 202.16357, 202.16296, 202.16333, 202.16342, 202.16371, 202.16367, 202.16348, 202.16324, 202.16299, 202.16225, 202.16251, 202.16351, 202.16528, 202.1601, 202.15561, 202.14296, 202.13995, 202.11896, 202.11909, 202.12131, 202.1273, 202.13329, 202.11716, 202.09338, 201.93658, 201.80626, 201.64171, 201.77411, 201.57242, 201.57214, 201.39615, 201.59508, 201.46597, 201.6857, 201.57092, 201.59845, 201.40837, 201.56891, 201.77933, 201.92172, 201.95352, 201.97815, 202.10938, 202.15511, 202.23477, 202.15749, 202.05634, 201.99504, 201.96783, 201.98001, 201.98398, 202.00468, 202.02626, 202.05249, 202.07529, 202.05533, 201.99432, 201.86716, 201.86563, 201.84171, 201.75644, 201.75635, 201.76349, 201.78564, 201.79755, 201.81969, 201.80173, 201.79211, 201.79025, 201.78403, 201.77176, 201.78416, 201.78873, 201.8017, 201.80255, 201.81805, 201.82837, 201.83914, 201.84976, 201.86165, 201.87027, 201.8718, 201.87296, 201.87878, 201.87775, 201.87961, 201.88028, 201.881, 201.8817, 201.89059, 201.89464, 201.89905, 201.92111, 201.94559, 201.94852, 201.94836, 201.91815, 201.91806, 201.91824, 201.91284, 201.91016, 202.08496, 202.02127, 201.94896, 201.95282, 201.95348, 202.02203, 202.09033, 202.3726, 202.61034, 202.86432, 202.99681, 202.96916, 202.83986, 202.64748, 202.48842, 202.20627, 201.92667, 201.75287, 201.51718, 201.27728, 201.06158, 200.60344, 200.23715, 200.0583, 199.89334, 199.93542, 200.02415, 200.22774, 200.50821, 200.67734, 200.95941, 201.11719, 201.14714, 201.19501, 201.24245, 201.26257, 201.31772, 201.3342, 201.35437, 201.45229, 201.47946, 201.4977, 201.51614, 201.51184, 201.50754, 201.45302, 201.40372, 201.37447, 201.34656, 201.30402, 201.27737, 201.40762, 201.618, 201.58005, 201.56801, 201.60287, 201.61725, 201.66013, 201.74344, 201.79333, 201.85835, 201.88057, 201.93881, 202.03464, 202.13239, 202.14883, 202.15302, 202.09126, 202.01477, 202.10638, 202.05472, 202.11604, 202.23492, 202.26691, 202.28964, 202.31996, 202.39017, 202.39993, 202.4697, 202.51376, 202.55083, 202.59076, 202.62119, 202.63907, 202.7173, 202.76694, 202.76767, 202.74013, 202.70676, 202.68253, 202.65186, 202.67659, 202.69179, 202.66821, 202.61459, 202.36734, 202.26871, 202.4437, 202.37177, 202.56581, 202.49937, 202.66005, 202.57603, 202.94435, 202.93919, 203.13162, 203.24413, 203.31256, 203.42871, 203.51672, 203.52858, 203.57092, 203.565, 203.55199, 203.53818, 203.52292, 203.5152, 203.54451, 203.62378, 203.60838, 203.61391, 203.60892, 203.55331, 203.37006, 203.28703, 203.28993, 203.35254, 203.40929, 203.41638, 203.44513, 203.46657, 203.46547, 203.429, 203.31511, 203.4061, 203.48914, 203.53503, 203.59262, 203.65742, 203.63539, 203.63312, 203.60635, 203.60915, 203.61412, 203.62956, 203.62004, 203.625, 203.65361, 203.52901, 203.46808, 203.46506, 203.38438, 203.31828, 203.28093, 203.23338, 203.21457, 203.20503, 203.12196, 203.10719, 203.14948, 203.17805, 203.19992, 203.09988, 202.96286, 202.8961, 202.812, 202.8333, 202.82564, 202.81128, 202.8084, 202.80797, 202.80739, 202.81134, 202.82489, 202.8428, 202.87201, 202.89813, 202.92232, 202.94629, 202.96838, 202.96664, 202.95778, 202.94748, 202.9353, 202.92906, 202.93542, 202.94101, 202.94913, 202.95529, 202.96252, 202.96552, 202.96555, 202.96112, 202.98053, 203.0023, 202.97943, 202.97192, 202.95642, 202.93996, 202.92365, 202.92102, 202.92496, 202.94044, 202.96301, 202.97821, 202.98665, 202.99504, 203.00566, 203.02194, 203.04877, 203.07214, 203.09891, 203.10652, 203.11713, 203.11668, 203.11559, 203.11325, 203.11592, 203.11638, 203.1167, 203.11702, 203.11824, 203.11873, 203.12201, 203.12527, 203.13324, 203.13902, 203.14098, 203.15677, 203.13553, 203.10744, 203.07793, 203.03212, 203.0307, 203.02977, 203.02969, 203.02979, 203.04007, 203.04298, 203.04294, 203.04285, 203.04483, 203.04678, 203.04562, 203.04498, 203.0493, 203.05238, 203.05264, 203.05299, 203.05763, 203.06442, 203.05917, 203.0807, 203.07274, 203.06696, 203.05478, 203.05649, 203.05797, 203.07349, 203.09569, 203.09064, 203.08601, 203.07912, 203.07233, 203.05333, 203.03387, 202.98355, 202.93149, 202.9063, 202.87793, 202.73894, 202.6922, 202.6945, 202.70287, 202.70016, 202.70294, 202.69359, 202.69612, 202.69342, 202.69316, 202.68307, 202.68294, 202.70567, 202.73196, 202.75328, 202.76709, 202.7859, 202.79614, 202.78931, 202.79361, 202.80089, 202.80484, 202.79842, 202.79944, 202.80173, 202.80206, 202.80106, 202.8046, 202.80765, 202.8103, 202.81949, 202.83673, 202.86252, 202.8887, 202.89922, 202.89955, 202.89221, 202.87962, 202.87511, 202.85786, 202.84914, 202.84824, 202.85764, 202.85899, 202.85629, 202.85338, 202.85724, 202.85892, 202.86238, 202.86356, 202.85338, 202.85036, 202.83812, 202.83669, 202.83536, 202.83469, 202.83389, 202.83389, 202.83252, 202.8317, 202.82637, 202.82463, 202.82439, 202.82524, 202.83871, 202.84566, 202.84563, 202.84613, 202.84497, 202.84407, 202.84488, 202.84247, 202.84444, 202.84186, 202.84129, 202.84103, 202.84393, 202.84624, 202.85213, 202.85628, 202.85579, 202.8553, 202.85504, 202.85396, 202.85477, 202.85513, 202.85503, 202.85428, 202.85602, 202.85593, 202.85602, 202.85428]
position_center_b = [211.99899, 211.99385, 211.99333, 211.993, 211.99716, 212.00002, 212.00124, 212.00327, 212.0033, 212.00394, 212.00377, 212.00385, 212.00145, 212.00143, 212.00209, 212.00204, 212.00159, 212.0014, 212.00098, 212.00041, 212.00029, 212.00002, 212.00005, 211.99992, 211.99777, 211.99725, 211.99736, 211.99753, 211.99792, 211.99776, 211.99757, 211.99722, 211.99626, 211.98962, 211.98416, 211.9852, 211.98311, 211.99974, 211.99104, 211.98848, 211.99565, 212.03583, 212.06172, 212.05948, 212.06404, 212.06639, 212.07437, 212.07764, 212.07735, 212.07309, 212.07109, 212.06369, 212.05577, 212.05325, 212.04979, 212.04677, 212.04495, 212.04306, 212.04271, 212.04301, 212.04257, 212.0419, 212.04082, 212.04227, 212.04303, 212.04289, 212.0423, 212.04176, 212.04172, 212.04173, 212.04138, 212.04225, 212.0394, 212.03708, 212.03157, 212.03549, 212.04065, 212.04581, 212.04852, 212.05576, 212.0611, 212.06657, 212.07239, 212.07655, 212.08955, 212.11252, 212.12375, 212.14232, 212.16141, 212.16042, 212.17386, 212.18352, 212.18443, 212.18253, 212.17113, 212.17232, 212.15953, 212.13704, 212.12521, 212.10727, 212.08731, 212.07964, 212.07097, 212.05574, 212.05147, 212.04375, 212.03879, 212.04646, 212.04977, 212.06563, 212.0712, 212.08231, 212.09413, 212.09608, 212.08324, 212.06839, 212.07228, 212.07503, 212.07806, 212.08572, 212.10326, 212.13002, 212.15536, 212.17857, 212.19823, 212.20691, 212.22528, 212.23701, 212.24553, 212.252, 212.26067, 212.26164, 212.26418, 212.26767, 212.26662, 212.26378, 212.25832, 212.25687, 212.25507, 212.241, 212.23734, 212.22668, 212.21591, 212.21082, 212.20496, 212.19202, 212.19106, 212.18231, 212.17683, 212.17627, 212.1738, 212.15776, 212.15784, 212.15105, 212.1427, 212.13863, 212.13498, 212.13062, 212.12988, 212.12242, 212.11728, 212.11357, 212.10887, 212.09926, 212.09775, 212.09457, 212.08931, 212.08458, 212.07899, 212.07214, 212.06906, 212.06168, 212.05458, 212.05127, 212.04662, 212.04109, 212.0385, 212.03731, 212.03729, 212.03319, 212.03659, 212.04478, 212.04642, 212.04852, 212.05588, 212.0612, 212.06578, 212.06871, 212.07628, 212.08597, 212.08748, 212.09358, 212.10272, 212.11407, 212.12508, 212.10713, 212.09187, 212.13269, 212.12898, 212.10458, 212.0956, 212.08824, 212.08182, 212.08244, 212.08185, 212.08148, 212.07994, 212.07898, 212.07913, 212.07895, 212.07326, 212.0713, 212.06824, 212.06764, 212.06538, 212.06538, 212.06485, 212.06461, 212.06485, 212.06528, 212.06718, 212.0692, 212.06992, 212.07043, 212.06982, 212.07083, 212.07187, 212.07143, 212.06918, 212.06902, 212.0696, 212.06979, 212.07027, 212.06911, 212.06816, 212.06616, 212.06563, 212.06044, 212.05699, 212.05106, 212.05096, 212.05174, 212.05211, 212.05568, 212.05934, 212.06261, 212.06538, 212.0656, 212.06575, 212.0648, 212.0649, 212.06488, 212.06479, 212.0649, 212.06451, 212.06419, 212.06383, 212.06348, 212.06297, 212.063, 212.06302, 212.06302, 212.06398, 212.06413, 212.06427, 212.064, 212.06371, 212.06363, 212.06416, 212.06421, 212.06422, 212.06389, 212.0641, 212.06403, 212.06432, 212.06442, 212.06447, 212.06462, 212.06471, 212.06471, 212.06305, 212.06381, 212.06239, 212.06158, 212.06154, 212.06645, 212.06673, 212.06709, 212.0672, 212.06718, 212.06728, 212.06721, 212.06725, 212.06726, 212.06728, 212.067, 212.06699, 212.06691, 212.06683, 212.06638, 212.06618, 212.06693, 212.06667, 212.06844, 212.06847, 212.06824, 212.06824, 212.06827, 212.06659, 211.98788, 211.97786, 211.98058, 211.99011, 211.98299, 211.97202, 211.96581, 211.97514, 211.95709, 211.96764, 211.96567, 211.96732, 211.94774, 211.94426, 211.92618, 211.96056, 211.95317, 211.94052, 211.93976, 211.95232, 211.93471, 211.88739, 211.92258, 211.98106, 212.04799, 212.05756, 212.06142, 212.06653, 212.06891, 212.07222, 212.07457, 212.06961, 212.0537, 212.01944, 212.01315, 212.0132, 212.0305, 212.03923, 212.03981, 212.04254, 212.04285, 212.04436, 212.04491, 212.04181, 212.0403, 212.04088, 212.04401, 212.04585, 212.04973, 212.05167, 212.05586, 212.0563, 212.05606, 212.05629, 212.05569, 212.05627, 212.05548, 212.05524, 212.05545, 212.05545, 212.05756, 212.05779, 212.05861, 212.05939, 212.05971, 212.0603, 212.06035, 212.06236, 212.06409, 212.06665, 212.07063, 212.07112, 212.07108, 212.06989, 212.06996, 212.0699, 212.06839, 212.06656, 212.0426, 212.00911, 211.97658, 211.96158, 211.97449, 211.91551, 211.8589, 211.86307, 211.87297, 211.88217, 211.88376, 211.87943, 211.87553, 211.8688, 211.86806, 211.86191, 211.89357, 211.90958, 211.91254, 211.92046, 211.9409, 211.961, 211.96625, 212.03087, 212.08592, 212.10976, 212.10219, 212.06355, 212.01646, 212.00026, 211.96747, 211.93698, 211.89822, 211.84398, 211.81679, 211.84601, 211.92329, 211.98076, 212.00606, 212.04271, 212.06261, 212.07504, 212.0974, 212.12363, 212.13716, 212.14568, 212.15027, 212.15923, 212.1553, 212.1438, 212.1297, 212.12228, 212.12306, 212.11122, 212.13057, 212.11951, 212.13785, 212.15448, 212.16119, 212.16812, 212.16553, 212.16197, 212.16269, 212.17169, 212.18338, 212.18614, 212.18817, 212.18896, 212.17451, 212.13889, 212.12033, 212.12175, 212.14326, 212.149, 212.14345, 212.15623, 212.16528, 212.16495, 212.17264, 212.17873, 212.1823, 212.18141, 212.18153, 212.18001, 212.17775, 212.16937, 212.16968, 212.17313, 212.17577, 212.18179, 212.18349, 212.17815, 212.17429, 212.17534, 212.1474, 212.11955, 212.12029, 212.10364, 212.10623, 212.09468, 212.10712, 212.08826, 212.114, 212.1273, 212.1311, 212.1656, 212.16904, 212.17053, 212.17511, 212.17694, 212.17879, 212.18178, 212.18407, 212.18365, 212.18454, 212.18536, 212.18571, 212.18776, 212.18658, 212.18037, 212.1769, 212.20337, 212.21149, 212.21207, 212.21155, 212.21207, 212.21425, 212.21611, 212.2155, 212.21165, 212.20833, 212.20915, 212.20468, 212.19942, 212.20753, 212.20818, 212.20833, 212.20731, 212.20583, 212.2061, 212.20605, 212.20502, 212.20491, 212.20409, 212.19429, 212.18739, 212.18246, 212.17818, 212.16672, 212.15645, 212.12764, 212.06917, 212.01889, 211.98677, 212.05058, 212.09137, 212.10677, 212.11946, 212.14421, 212.18184, 212.17104, 212.13301, 212.10713, 212.12712, 212.18628, 212.25768, 212.27579, 212.29253, 212.30896, 212.32733, 212.33177, 212.33653, 212.33783, 212.34036, 212.34218, 212.34592, 212.34592, 212.34641, 212.34862, 212.34958, 212.34943, 212.35156, 212.35422, 212.35585, 212.35977, 212.35992, 212.36014, 212.36064, 212.36072, 212.36168, 212.36192, 212.36195, 212.36208, 212.35529, 212.34886, 212.34671, 212.3481, 212.35196, 212.35689, 212.36356, 212.36385, 212.36679, 212.36797, 212.36874, 212.37146, 212.37228, 212.37251, 212.37282, 212.37354, 212.37386, 212.37393, 212.37523, 212.37529, 212.37466, 212.37473, 212.37465, 212.37468, 212.37138, 212.37251, 212.37135, 212.37099, 212.37082, 212.37044, 212.37061, 212.37004, 212.37083, 212.37, 212.36957, 212.36977, 212.36935, 212.36951, 212.36852, 212.36726, 212.3674, 212.36755, 212.36755, 212.36751, 212.36864, 212.3689, 212.3689, 212.3688, 212.36884, 212.36911, 212.36923, 212.36908, 212.36931, 212.36978, 212.36974, 212.36983, 212.36829, 212.36684, 212.3651, 212.35553, 212.34152, 212.33344, 212.32573, 212.32547, 212.32545, 212.33029, 212.33812, 212.34258, 212.34654, 212.34433, 212.34218, 212.34181, 212.34262, 212.34459, 212.34792, 212.34581, 212.34277, 212.33176, 212.33372, 212.33461, 212.33791, 212.34154, 212.33911, 212.33949, 212.33965, 212.34042, 212.34113, 212.34251, 212.3425, 212.34242, 212.34317, 212.343, 212.34348, 212.34476, 212.34543, 212.34755, 212.34836, 212.34984, 212.35124, 212.3519, 212.35211, 212.35074, 212.35043, 212.35019, 212.34891, 212.34901, 212.34904, 212.34914, 212.34959, 212.3502, 212.35045, 212.35085, 212.35109, 212.35066, 212.35023, 212.34991, 212.34981, 212.34991, 212.34978, 212.34807, 212.34753, 212.34785, 212.34814, 212.34749, 212.34738, 212.34605, 212.3448, 212.34398, 212.34416, 212.34303, 212.34328, 212.34329, 212.34471, 212.3457, 212.34694, 212.34683, 212.34694, 212.34694, 212.34749, 212.34729, 212.34741, 212.34827, 212.34738, 212.34729, 212.34731, 212.34859, 212.34998, 212.35063, 212.35255, 212.35442, 212.35515, 212.35568, 212.35617, 212.35648, 212.3566, 212.35689, 212.35687, 212.35669, 212.35666, 212.35663, 212.35643, 212.35632, 212.35635, 212.35635, 212.35637, 212.35573, 212.35567, 212.3557, 212.35638]

input_video_name = gs.input_video_name
input_images = gs.input_image
new_image_name = gs.new_image_name
out_put_video_name = gs.out_put_video_name

google_logo = "/Users/Allan/Desktop/xAd_Resource/google.jpg"
taobao_logo = "/Users/Allan/Desktop/xAd_Resource/tao.jpg"

def draw_some_on_the_frame(videoSrc, imgSrc1, imgSrc2):
    cap = cv2.VideoCapture(videoSrc)
    i = 0
    while True:
        ret , frame = cap.read()
        if ret:
            #cv2.putText(frame,"hello",(int(position_center_a[i]-150), int(position_center_b[i])+20),cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
            if(i <= len(position_center_a)):
                try:
                    outPath = save_images(i,frame)
                    put_image_to_video(outPath,imgSrc1,outPath,int(round(position_center_a[i]-70)),int(round(position_center_b[i]+10)),5)
                    if imgSrc2:
                        print(1)
                        #put_image_to_video(outPath,imgSrc2,outPath,int(round(position_center_a[i]+177)),int(round(position_center_b[i]+10)),3)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                except:
                    create_video_from_image("/Users/Allan/Desktop/xAd/videoImages/%s%d.jpg" % (gs.new_image_name,0),i)
                    print("except")

            else:
                create_video_from_image("/Users/Allan/Desktop/xAd/videoImages/%s%d.jpg" % (gs.new_image_name,0),i)
                print("1")
                break;

        else:
            create_video_from_image("/Users/Allan/Desktop/xAd/videoImages/%s%d.jpg" % (gs.new_image_name,0),i)
            print("2")
            break
        i +=1
        cv2.imshow("haha",frame)
    cap.release()
    cv2.destroyAllWindows()

def save_images(i, frame):
    imageName = ("%s%d.jpg"%(new_image_name,i))
    outPath = "./videoImages/%s" % imageName
    cv2.imwrite(outPath, frame)
    return outPath

def put_image_to_video(videoFramSrc, imageSrc, outPut, a,b, small_scall):
    bgFrame = cv2.imread(videoFramSrc)
    logo = cv2.imread(imageSrc)
    logo_width, logo_height = logo.shape[1]/small_scall, logo.shape[0]/small_scall

    new_logo = cv2.resize(logo, (logo_width, logo_height))
    #mask = 255 * np.ones(new_logo.shape, new_logo.dtype)

    center = (a, b)

    mix_clone = cv2.seamlessClone(new_logo, bgFrame, new_logo, center, cv2.MIXED_CLONE)
    cv2.imwrite(outPut, mix_clone)


def create_video_from_image(fristImage, num):
    cap = cv2.VideoCapture(fristImage)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)+0.5 )
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)+0.5)

    foucc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')

    videoWrite = cv2.VideoWriter(out_put_video_name, foucc, 20.0, (width, height))

    for i in range(0, num):
        imageName = ("/Users/Allan/Desktop/xAd/videoImages/%s%d.jpg"%(new_image_name,i))
        saveCap = cv2.VideoCapture(imageName)
        ret, frame = saveCap.read()

        if ret:
            videoWrite.write(frame)
        else:
            print("can not save this image")
            break

if __name__  == "__main__":
    start = time.clock()
    #draw_some_on_the_frame(args["out_path"], args["img1"], args["img2"])
    draw_some_on_the_frame(input_video_name, google_logo, taobao_logo)
    print "%s  %s"%("set_tracker_postion", time.clock() - start), "second"
    print("done")


