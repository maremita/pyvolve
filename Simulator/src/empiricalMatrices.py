# File with empirical matrices. For now, amino acid, and in the future, probably some codon ones.
import numpy as np


wag_freqs = [0.0866279, 0.0193078, 0.0570451, 0.0580589, 0.0384319, 0.0832518, 0.0244313, 0.048466, 0.0620286, 0.086209, 0.0195027, 0.0390894, 0.0457631, 0.0367281, 0.043972, 0.0695179, 0.0610127, 0.0708956, 0.0143859, 0.0352742]
wag_matrix = np.array([
[0.000000000000000000e+00, 1.027039999999999953e+00, 7.389980000000000437e-01, 1.582850000000000090e+00, 2.104939999999999867e-01, 1.416719999999999979e+00, 3.169540000000000135e-01, 1.933350000000000068e-01, 9.062649999999999872e-01, 3.979150000000000187e-01, 8.934959999999999569e-01, 5.098479999999999679e-01, 1.438549999999999995e+00, 9.085980000000000167e-01, 5.515710000000000335e-01, 3.370789999999999953e+00, 2.121109999999999829e+00, 2.006009999999999849e+00, 1.131329999999999975e-01, 2.407350000000000045e-01],
[1.027039999999999953e+00, 0.000000000000000000e+00, 3.029489999999999961e-02, 2.135199999999999945e-02, 3.980199999999999849e-01, 3.066740000000000022e-01, 2.489719999999999989e-01, 1.701350000000000084e-01, 7.403389999999999971e-02, 3.842869999999999897e-01, 3.904819999999999958e-01, 2.652559999999999918e-01, 1.094040000000000012e-01, 9.881790000000000018e-02, 5.281909999999999661e-01, 1.407659999999999911e+00, 5.129839999999999955e-01, 1.002140000000000031e+00, 7.170699999999999852e-01, 5.438330000000000108e-01],
[7.389980000000000437e-01, 3.029489999999999961e-02, 0.000000000000000000e+00, 6.174159999999999648e+00, 4.673039999999999833e-02, 8.655840000000000201e-01, 9.306759999999999478e-01, 3.943699999999999983e-02, 4.798549999999999760e-01, 8.480469999999999675e-02, 1.037539999999999990e-01, 5.429420000000000357e+00, 4.239840000000000275e-01, 6.167829999999999702e-01, 1.473039999999999905e-01, 1.071760000000000046e+00, 3.748659999999999770e-01, 1.523349999999999982e-01, 1.297669999999999935e-01, 3.257109999999999728e-01],
[1.582850000000000090e+00, 2.135199999999999945e-02, 6.174159999999999648e+00, 0.000000000000000000e+00, 8.113389999999999491e-02, 5.677170000000000272e-01, 5.700250000000000039e-01, 1.273950000000000082e-01, 2.584429999999999783e+00, 1.542630000000000112e-01, 3.151240000000000152e-01, 9.471979999999999844e-01, 6.823550000000000448e-01, 5.469470000000000276e+00, 4.391570000000000196e-01, 7.049389999999999823e-01, 8.227649999999999686e-01, 5.887310000000000043e-01, 1.565570000000000017e-01, 1.963030000000000053e-01],
[2.104939999999999867e-01, 3.980199999999999849e-01, 4.673039999999999833e-02, 8.113389999999999491e-02, 0.000000000000000000e+00, 4.993100000000000316e-02, 6.793709999999999471e-01, 1.059469999999999912e+00, 8.883599999999999830e-02, 2.115169999999999995e+00, 1.190630000000000077e+00, 9.616210000000000035e-02, 1.614440000000000042e-01, 9.992080000000000406e-02, 1.027109999999999967e-01, 5.459310000000000551e-01, 1.719030000000000002e-01, 6.498920000000000252e-01, 1.529640000000000111e+00, 6.454279999999999795e+00],
[1.416719999999999979e+00, 3.066740000000000022e-01, 8.655840000000000201e-01, 5.677170000000000272e-01, 4.993100000000000316e-02, 0.000000000000000000e+00, 2.494099999999999928e-01, 3.045010000000000078e-02, 3.735580000000000012e-01, 6.130370000000000263e-02, 1.741000000000000048e-01, 1.125559999999999894e+00, 2.435700000000000087e-01, 3.300520000000000120e-01, 5.846649999999999903e-01, 1.341820000000000013e+00, 2.258330000000000060e-01, 1.872469999999999968e-01, 3.369829999999999770e-01, 1.036040000000000016e-01],
[3.169540000000000135e-01, 2.489719999999999989e-01, 9.306759999999999478e-01, 5.700250000000000039e-01, 6.793709999999999471e-01, 2.494099999999999928e-01, 0.000000000000000000e+00, 1.381900000000000073e-01, 8.904320000000000013e-01, 4.994620000000000171e-01, 4.041409999999999725e-01, 3.956290000000000084e+00, 6.961979999999999835e-01, 4.294109999999999872e+00, 2.137150000000000105e+00, 7.401689999999999658e-01, 4.733069999999999777e-01, 1.183580000000000049e-01, 2.625689999999999968e-01, 3.873439999999999994e+00],
[1.933350000000000068e-01, 1.701350000000000084e-01, 3.943699999999999983e-02, 1.273950000000000082e-01, 1.059469999999999912e+00, 3.045010000000000078e-02, 1.381900000000000073e-01, 0.000000000000000000e+00, 3.238320000000000087e-01, 3.170970000000000066e+00, 4.257460000000000022e+00, 5.542359999999999509e-01, 9.992879999999999818e-02, 1.139170000000000044e-01, 1.869790000000000063e-01, 3.194400000000000017e-01, 1.458159999999999901e+00, 7.821299999999999919e+00, 2.124830000000000052e-01, 4.201699999999999879e-01],
[9.062649999999999872e-01, 7.403389999999999971e-02, 4.798549999999999760e-01, 2.584429999999999783e+00, 8.883599999999999830e-02, 3.735580000000000012e-01, 8.904320000000000013e-01, 3.238320000000000087e-01, 0.000000000000000000e+00, 2.575549999999999784e-01, 9.342759999999999954e-01, 3.012010000000000076e+00, 5.568959999999999466e-01, 3.894899999999999807e+00, 5.351420000000000066e+00, 9.671300000000000452e-01, 1.386980000000000102e+00, 3.054339999999999833e-01, 1.375049999999999883e-01, 1.332639999999999936e-01],
[3.979150000000000187e-01, 3.842869999999999897e-01, 8.480469999999999675e-02, 1.542630000000000112e-01, 2.115169999999999995e+00, 6.130370000000000263e-02, 4.994620000000000171e-01, 3.170970000000000066e+00, 2.575549999999999784e-01, 0.000000000000000000e+00, 4.854020000000000223e+00, 1.315280000000000060e-01, 4.158439999999999914e-01, 8.694889999999999564e-01, 4.976709999999999745e-01, 3.447390000000000176e-01, 3.266220000000000234e-01, 1.800340000000000051e+00, 6.653090000000000392e-01, 3.986179999999999723e-01],
[8.934959999999999569e-01, 3.904819999999999958e-01, 1.037539999999999990e-01, 3.151240000000000152e-01, 1.190630000000000077e+00, 1.741000000000000048e-01, 4.041409999999999725e-01, 4.257460000000000022e+00, 9.342759999999999954e-01, 4.854020000000000223e+00, 0.000000000000000000e+00, 1.982210000000000083e-01, 1.713290000000000091e-01, 1.545260000000000078e+00, 6.831620000000000470e-01, 4.939049999999999829e-01, 1.516119999999999912e+00, 2.058450000000000113e+00, 5.157059999999999977e-01, 4.284370000000000123e-01],
[5.098479999999999679e-01, 2.652559999999999918e-01, 5.429420000000000357e+00, 9.471979999999999844e-01, 9.616210000000000035e-02, 1.125559999999999894e+00, 3.956290000000000084e+00, 5.542359999999999509e-01, 3.012010000000000076e+00, 1.315280000000000060e-01, 1.982210000000000083e-01, 0.000000000000000000e+00, 1.950810000000000044e-01, 1.543639999999999901e+00, 6.353459999999999663e-01, 3.974229999999999929e+00, 2.030060000000000198e+00, 1.962460000000000038e-01, 7.191670000000000007e-02, 1.086000000000000076e+00],
[1.438549999999999995e+00, 1.094040000000000012e-01, 4.239840000000000275e-01, 6.823550000000000448e-01, 1.614440000000000042e-01, 2.435700000000000087e-01, 6.961979999999999835e-01, 9.992879999999999818e-02, 5.568959999999999466e-01, 4.158439999999999914e-01, 1.713290000000000091e-01, 1.950810000000000044e-01, 0.000000000000000000e+00, 9.333719999999999795e-01, 6.794890000000000096e-01, 1.613280000000000047e+00, 7.953839999999999799e-01, 3.148869999999999725e-01, 1.394050000000000011e-01, 2.160459999999999881e-01],
[9.085980000000000167e-01, 9.881790000000000018e-02, 6.167829999999999702e-01, 5.469470000000000276e+00, 9.992080000000000406e-02, 3.300520000000000120e-01, 4.294109999999999872e+00, 1.139170000000000044e-01, 3.894899999999999807e+00, 8.694889999999999564e-01, 1.545260000000000078e+00, 1.543639999999999901e+00, 9.333719999999999795e-01, 0.000000000000000000e+00, 3.035499999999999865e+00, 1.028869999999999951e+00, 8.579280000000000239e-01, 3.012810000000000210e-01, 2.157370000000000121e-01, 2.277099999999999957e-01],
[5.515710000000000335e-01, 5.281909999999999661e-01, 1.473039999999999905e-01, 4.391570000000000196e-01, 1.027109999999999967e-01, 5.846649999999999903e-01, 2.137150000000000105e+00, 1.869790000000000063e-01, 5.351420000000000066e+00, 4.976709999999999745e-01, 6.831620000000000470e-01, 6.353459999999999663e-01, 6.794890000000000096e-01, 3.035499999999999865e+00, 0.000000000000000000e+00, 1.224189999999999889e+00, 5.544130000000000447e-01, 2.518489999999999895e-01, 1.163920000000000066e+00, 3.815330000000000110e-01],
[3.370789999999999953e+00, 1.407659999999999911e+00, 1.071760000000000046e+00, 7.049389999999999823e-01, 5.459310000000000551e-01, 1.341820000000000013e+00, 7.401689999999999658e-01, 3.194400000000000017e-01, 9.671300000000000452e-01, 3.447390000000000176e-01, 4.939049999999999829e-01, 3.974229999999999929e+00, 1.613280000000000047e+00, 1.028869999999999951e+00, 1.224189999999999889e+00, 0.000000000000000000e+00, 4.378020000000000245e+00, 2.327390000000000014e-01, 5.237420000000000408e-01, 7.869930000000000536e-01],
[2.121109999999999829e+00, 5.129839999999999955e-01, 3.748659999999999770e-01, 8.227649999999999686e-01, 1.719030000000000002e-01, 2.258330000000000060e-01, 4.733069999999999777e-01, 1.458159999999999901e+00, 1.386980000000000102e+00, 3.266220000000000234e-01, 1.516119999999999912e+00, 2.030060000000000198e+00, 7.953839999999999799e-01, 8.579280000000000239e-01, 5.544130000000000447e-01, 4.378020000000000245e+00, 0.000000000000000000e+00, 1.388230000000000075e+00, 1.108640000000000042e-01, 2.911480000000000179e-01],
[2.006009999999999849e+00, 1.002140000000000031e+00, 1.523349999999999982e-01, 5.887310000000000043e-01, 6.498920000000000252e-01, 1.872469999999999968e-01, 1.183580000000000049e-01, 7.821299999999999919e+00, 3.054339999999999833e-01, 1.800340000000000051e+00, 2.058450000000000113e+00, 1.962460000000000038e-01, 3.148869999999999725e-01, 3.012810000000000210e-01, 2.518489999999999895e-01, 2.327390000000000014e-01, 1.388230000000000075e+00, 0.000000000000000000e+00, 3.653689999999999993e-01, 3.147300000000000098e-01],
[1.131329999999999975e-01, 7.170699999999999852e-01, 1.297669999999999935e-01, 1.565570000000000017e-01, 1.529640000000000111e+00, 3.369829999999999770e-01, 2.625689999999999968e-01, 2.124830000000000052e-01, 1.375049999999999883e-01, 6.653090000000000392e-01, 5.157059999999999977e-01, 7.191670000000000007e-02, 1.394050000000000011e-01, 2.157370000000000121e-01, 1.163920000000000066e+00, 5.237420000000000408e-01, 1.108640000000000042e-01, 3.653689999999999993e-01, 0.000000000000000000e+00, 2.485390000000000210e+00],
[2.407350000000000045e-01, 5.438330000000000108e-01, 3.257109999999999728e-01, 1.963030000000000053e-01, 6.454279999999999795e+00, 1.036040000000000016e-01, 3.873439999999999994e+00, 4.201699999999999879e-01, 1.332639999999999936e-01, 3.986179999999999723e-01, 4.284370000000000123e-01, 1.086000000000000076e+00, 2.160459999999999881e-01, 2.277099999999999957e-01, 3.815330000000000110e-01, 7.869930000000000536e-01, 2.911480000000000179e-01, 3.147300000000000098e-01, 2.485390000000000210e+00, 0.000000000000000000e+00]
])

lg_freqs  = [0.079066, 0.012937, 0.053052, 0.071586, 0.042302, 0.057337, 0.022355, 0.062157, 0.0646, 0.099081, 0.022951, 0.041977, 0.04404, 0.040767, 0.055941, 0.061197, 0.053287, 0.069147, 0.012066, 0.034155]
lg_matrix = np.array([
[0.000000000000000000e+00, 2.489084000000000074e+00, 3.951439999999999952e-01, 1.038545000000000051e+00, 2.537010000000000098e-01, 2.066040000000000099e+00, 3.588580000000000103e-01, 1.498299999999999910e-01, 5.365180000000000504e-01, 3.953369999999999940e-01, 1.124034999999999895e+00, 2.768180000000000085e-01, 1.177651000000000003e+00, 9.698940000000000339e-01, 4.250929999999999986e-01, 4.727181999999999995e+00, 2.139501000000000097e+00, 2.547870000000000079e+00, 1.807169999999999888e-01, 2.189589999999999870e-01],
[2.489084000000000074e+00, 0.000000000000000000e+00, 6.255600000000000049e-02, 3.498999999999999940e-03, 1.105250999999999983e+00, 5.692650000000000210e-01, 6.405429999999999735e-01, 3.206269999999999953e-01, 1.326600000000000001e-02, 5.940069999999999517e-01, 8.936800000000000299e-01, 5.287680000000000158e-01, 7.538200000000000456e-02, 8.480799999999999450e-02, 5.345509999999999984e-01, 2.784478000000000009e+00, 1.143480000000000052e+00, 1.959290999999999894e+00, 6.701279999999999459e-01, 1.165532000000000012e+00],
[3.951439999999999952e-01, 6.255600000000000049e-02, 0.000000000000000000e+00, 5.243870000000000253e+00, 1.741600000000000092e-02, 8.449259999999999549e-01, 9.271139999999999937e-01, 1.068999999999999985e-02, 2.829590000000000161e-01, 1.507600000000000086e-02, 2.554800000000000126e-02, 5.076149000000000022e+00, 3.944559999999999733e-01, 5.233860000000000179e-01, 1.239539999999999947e-01, 1.240275000000000016e+00, 4.258600000000000163e-01, 3.796700000000000075e-02, 2.988999999999999990e-02, 1.351070000000000049e-01],
[1.038545000000000051e+00, 3.498999999999999940e-03, 5.243870000000000253e+00, 0.000000000000000000e+00, 1.881100000000000133e-02, 3.488470000000000182e-01, 4.238810000000000078e-01, 4.426499999999999879e-02, 1.807177000000000033e+00, 6.967299999999999882e-02, 1.737350000000000005e-01, 5.417119999999999713e-01, 4.194089999999999763e-01, 4.128591000000000122e+00, 3.639700000000000157e-01, 6.119729999999999892e-01, 6.045449999999999990e-01, 2.450340000000000018e-01, 7.785200000000000453e-02, 1.200370000000000048e-01],
[2.537010000000000098e-01, 1.105250999999999983e+00, 1.741600000000000092e-02, 1.881100000000000133e-02, 0.000000000000000000e+00, 8.958599999999999897e-02, 6.821390000000000509e-01, 1.112727000000000022e+00, 2.391799999999999829e-02, 2.592691999999999997e+00, 1.798853000000000035e+00, 8.952499999999999347e-02, 9.446400000000000630e-02, 3.585499999999999798e-02, 5.272199999999999803e-02, 3.618190000000000017e-01, 1.650010000000000088e-01, 6.546830000000000149e-01, 2.457120999999999889e+00, 7.803901999999999894e+00],
[2.066040000000000099e+00, 5.692650000000000210e-01, 8.449259999999999549e-01, 3.488470000000000182e-01, 8.958599999999999897e-02, 0.000000000000000000e+00, 3.114839999999999831e-01, 8.704999999999999197e-03, 2.966360000000000108e-01, 4.426100000000000173e-02, 1.395379999999999954e-01, 1.437645000000000062e+00, 1.969609999999999972e-01, 2.679590000000000027e-01, 3.901919999999999833e-01, 1.739989999999999926e+00, 1.298360000000000070e-01, 7.670100000000000529e-02, 2.684909999999999797e-01, 5.467899999999999844e-02],
[3.588580000000000103e-01, 6.405429999999999735e-01, 9.271139999999999937e-01, 4.238810000000000078e-01, 6.821390000000000509e-01, 3.114839999999999831e-01, 0.000000000000000000e+00, 1.088820000000000066e-01, 6.972639999999999949e-01, 3.663170000000000037e-01, 4.424719999999999764e-01, 4.509237999999999857e+00, 5.088510000000000533e-01, 4.813505000000000145e+00, 2.426600999999999786e+00, 9.900120000000000031e-01, 5.842619999999999481e-01, 1.190129999999999938e-01, 5.970539999999999736e-01, 5.306834000000000273e+00],
[1.498299999999999910e-01, 3.206269999999999953e-01, 1.068999999999999985e-02, 4.426499999999999879e-02, 1.112727000000000022e+00, 8.704999999999999197e-03, 1.088820000000000066e-01, 0.000000000000000000e+00, 1.590689999999999882e-01, 4.145067000000000057e+00, 4.273607000000000156e+00, 1.915030000000000066e-01, 7.828100000000000336e-02, 7.285400000000000209e-02, 1.269909999999999928e-01, 6.410499999999999532e-02, 1.033738999999999963e+00, 6.491069999999999895e-01, 1.116599999999999954e-01, 2.325230000000000075e-01],
[5.365180000000000504e-01, 1.326600000000000001e-02, 2.829590000000000161e-01, 1.807177000000000033e+00, 2.391799999999999829e-02, 2.966360000000000108e-01, 6.972639999999999949e-01, 1.590689999999999882e-01, 0.000000000000000000e+00, 1.375000000000000111e-01, 6.566039999999999655e-01, 2.145077999999999818e+00, 3.903220000000000023e-01, 3.234293999999999780e+00, 6.326067000000000107e+00, 7.486829999999999874e-01, 1.136862999999999957e+00, 1.852020000000000055e-01, 4.990599999999999897e-02, 1.319319999999999937e-01],
[3.953369999999999940e-01, 5.940069999999999517e-01, 1.507600000000000086e-02, 6.967299999999999882e-02, 2.592691999999999997e+00, 4.426100000000000173e-02, 3.663170000000000037e-01, 4.145067000000000057e+00, 1.375000000000000111e-01, 0.000000000000000000e+00, 6.312357999999999691e+00, 6.842700000000000171e-02, 2.490600000000000036e-01, 5.824570000000000025e-01, 3.018480000000000052e-01, 1.822870000000000046e-01, 3.029359999999999831e-01, 1.702744999999999953e+00, 6.196319999999999606e-01, 2.996480000000000254e-01],
[1.124034999999999895e+00, 8.936800000000000299e-01, 2.554800000000000126e-02, 1.737350000000000005e-01, 1.798853000000000035e+00, 1.395379999999999954e-01, 4.424719999999999764e-01, 4.273607000000000156e+00, 6.566039999999999655e-01, 6.312357999999999691e+00, 0.000000000000000000e+00, 3.710040000000000004e-01, 9.984899999999999332e-02, 1.672568999999999972e+00, 4.841329999999999800e-01, 3.469599999999999906e-01, 2.020366000000000106e+00, 1.898717999999999906e+00, 6.961749999999999883e-01, 4.813060000000000116e-01],
[2.768180000000000085e-01, 5.287680000000000158e-01, 5.076149000000000022e+00, 5.417119999999999713e-01, 8.952499999999999347e-02, 1.437645000000000062e+00, 4.509237999999999857e+00, 1.915030000000000066e-01, 2.145077999999999818e+00, 6.842700000000000171e-02, 3.710040000000000004e-01, 0.000000000000000000e+00, 1.617869999999999864e-01, 1.695751999999999926e+00, 7.518780000000000463e-01, 4.008358000000000310e+00, 2.000678999999999874e+00, 8.368799999999999850e-02, 4.537599999999999967e-02, 6.120250000000000412e-01],
[1.177651000000000003e+00, 7.538200000000000456e-02, 3.944559999999999733e-01, 4.194089999999999763e-01, 9.446400000000000630e-02, 1.969609999999999972e-01, 5.088510000000000533e-01, 7.828100000000000336e-02, 3.903220000000000023e-01, 2.490600000000000036e-01, 9.984899999999999332e-02, 1.617869999999999864e-01, 0.000000000000000000e+00, 6.242940000000000156e-01, 3.325330000000000230e-01, 1.338132000000000099e+00, 5.714679999999999760e-01, 2.965010000000000145e-01, 9.513099999999999334e-02, 8.961299999999999821e-02],
[9.698940000000000339e-01, 8.480799999999999450e-02, 5.233860000000000179e-01, 4.128591000000000122e+00, 3.585499999999999798e-02, 2.679590000000000027e-01, 4.813505000000000145e+00, 7.285400000000000209e-02, 3.234293999999999780e+00, 5.824570000000000025e-01, 1.672568999999999972e+00, 1.695751999999999926e+00, 6.242940000000000156e-01, 0.000000000000000000e+00, 2.807907999999999848e+00, 1.223827999999999916e+00, 1.080135999999999985e+00, 2.103319999999999912e-01, 2.361989999999999923e-01, 2.573360000000000092e-01],
[4.250929999999999986e-01, 5.345509999999999984e-01, 1.239539999999999947e-01, 3.639700000000000157e-01, 5.272199999999999803e-02, 3.901919999999999833e-01, 2.426600999999999786e+00, 1.269909999999999928e-01, 6.326067000000000107e+00, 3.018480000000000052e-01, 4.841329999999999800e-01, 7.518780000000000463e-01, 3.325330000000000230e-01, 2.807907999999999848e+00, 0.000000000000000000e+00, 8.581509999999999971e-01, 5.789870000000000294e-01, 1.708870000000000111e-01, 5.936069999999999958e-01, 3.144399999999999973e-01],
[4.727181999999999995e+00, 2.784478000000000009e+00, 1.240275000000000016e+00, 6.119729999999999892e-01, 3.618190000000000017e-01, 1.739989999999999926e+00, 9.900120000000000031e-01, 6.410499999999999532e-02, 7.486829999999999874e-01, 1.822870000000000046e-01, 3.469599999999999906e-01, 4.008358000000000310e+00, 1.338132000000000099e+00, 1.223827999999999916e+00, 8.581509999999999971e-01, 0.000000000000000000e+00, 6.472279000000000337e+00, 9.836899999999999811e-02, 2.488619999999999999e-01, 4.005469999999999864e-01],
[2.139501000000000097e+00, 1.143480000000000052e+00, 4.258600000000000163e-01, 6.045449999999999990e-01, 1.650010000000000088e-01, 1.298360000000000070e-01, 5.842619999999999481e-01, 1.033738999999999963e+00, 1.136862999999999957e+00, 3.029359999999999831e-01, 2.020366000000000106e+00, 2.000678999999999874e+00, 5.714679999999999760e-01, 1.080135999999999985e+00, 5.789870000000000294e-01, 6.472279000000000337e+00, 0.000000000000000000e+00, 2.188158000000000047e+00, 1.408250000000000057e-01, 2.458410000000000040e-01],
[2.547870000000000079e+00, 1.959290999999999894e+00, 3.796700000000000075e-02, 2.450340000000000018e-01, 6.546830000000000149e-01, 7.670100000000000529e-02, 1.190129999999999938e-01, 6.491069999999999895e-01, 1.852020000000000055e-01, 1.702744999999999953e+00, 1.898717999999999906e+00, 8.368799999999999850e-02, 2.965010000000000145e-01, 2.103319999999999912e-01, 1.708870000000000111e-01, 9.836899999999999811e-02, 2.188158000000000047e+00, 0.000000000000000000e+00, 1.895100000000000118e-01, 2.493130000000000068e-01],
[1.807169999999999888e-01, 6.701279999999999459e-01, 2.988999999999999990e-02, 7.785200000000000453e-02, 2.457120999999999889e+00, 2.684909999999999797e-01, 5.970539999999999736e-01, 1.116599999999999954e-01, 4.990599999999999897e-02, 6.196319999999999606e-01, 6.961749999999999883e-01, 4.537599999999999967e-02, 9.513099999999999334e-02, 2.361989999999999923e-01, 5.936069999999999958e-01, 2.488619999999999999e-01, 1.408250000000000057e-01, 1.895100000000000118e-01, 0.000000000000000000e+00, 3.151815000000000033e+00],
[2.189589999999999870e-01, 1.165532000000000012e+00, 1.351070000000000049e-01, 1.200370000000000048e-01, 7.803901999999999894e+00, 5.467899999999999844e-02, 5.306834000000000273e+00, 2.325230000000000075e-01, 1.319319999999999937e-01, 2.996480000000000254e-01, 4.813060000000000116e-01, 6.120250000000000412e-01, 8.961299999999999821e-02, 2.573360000000000092e-01, 3.144399999999999973e-01, 4.005469999999999864e-01, 2.458410000000000040e-01, 2.493130000000000068e-01, 3.151815000000000033e+00, 0.000000000000000000e+00]
])


jtt_freqs = [0.076862, 0.020279, 0.051269, 0.06182, 0.04053, 0.074714, 0.022983, 0.052569, 0.059498, 0.091111, 0.023414, 0.042546, 0.050532, 0.041061, 0.051057, 0.068225, 0.058518, 0.066374, 0.014336, 0.032303]
jtt_matrix = np.array([
[0.000000000000000000e+00, 5.744780000000000442e-01, 8.274449999999999861e-01, 1.066680999999999990e+00, 1.382929999999999993e-01, 1.740159000000000011e+00, 2.199699999999999989e-01, 3.616840000000000055e-01, 3.694370000000000154e-01, 3.100069999999999770e-01, 4.693950000000000067e-01, 5.579669999999999908e-01, 1.959599000000000091e+00, 5.567250000000000254e-01, 5.316779999999999839e-01, 3.887094999999999967e+00, 4.582564999999999777e+00, 2.924160999999999788e+00, 8.432900000000000118e-02, 1.394920000000000049e-01],
[5.744780000000000442e-01, 0.000000000000000000e+00, 1.056249999999999967e-01, 5.390699999999999659e-02, 6.783350000000000213e-01, 5.463890000000000136e-01, 7.249980000000000313e-01, 1.505589999999999984e-01, 4.900899999999999701e-02, 1.645929999999999893e-01, 4.092020000000000102e-01, 3.133110000000000062e-01, 1.236529999999999990e-01, 9.130399999999999627e-02, 1.019843000000000055e+00, 2.155330999999999886e+00, 4.698229999999999906e-01, 6.213229999999999587e-01, 1.104181000000000079e+00, 2.114851999999999954e+00],
[8.274449999999999861e-01, 1.056249999999999967e-01, 0.000000000000000000e+00, 7.766556999999999711e+00, 3.252200000000000230e-02, 1.272434000000000065e+00, 1.032342000000000093e+00, 1.159680000000000016e-01, 2.824659999999999949e-01, 6.148599999999999899e-02, 1.900010000000000032e-01, 5.549529999999999852e+00, 1.271639999999999993e-01, 5.216460000000000541e-01, 1.548990000000000089e-01, 5.892680000000000140e-01, 4.251590000000000091e-01, 3.152610000000000134e-01, 5.746600000000000319e-02, 4.539520000000000222e-01],
[1.066680999999999990e+00, 5.390699999999999659e-02, 7.766556999999999711e+00, 0.000000000000000000e+00, 4.382899999999999990e-02, 1.115631999999999957e+00, 2.437680000000000125e-01, 1.117729999999999974e-01, 1.731684000000000001e+00, 9.748500000000000221e-02, 1.750839999999999896e-01, 5.781150000000000455e-01, 1.919939999999999980e-01, 3.417705999999999911e+00, 3.184830000000000161e-01, 3.124489999999999768e-01, 3.315839999999999899e-01, 4.652709999999999901e-01, 1.143809999999999966e-01, 6.345199999999999452e-02],
[1.382929999999999993e-01, 6.783350000000000213e-01, 3.252200000000000230e-02, 4.382899999999999990e-02, 0.000000000000000000e+00, 5.021199999999999969e-02, 4.534279999999999977e-01, 7.770899999999999475e-01, 2.452100000000000113e-02, 2.500293999999999794e+00, 4.361809999999999854e-01, 7.348100000000000465e-02, 1.484830000000000039e-01, 4.568300000000000138e-02, 6.531399999999999706e-02, 9.439710000000000045e-01, 1.389039999999999997e-01, 5.934779999999999500e-01, 5.379220000000000113e-01, 5.484236000000000111e+00],
[1.740159000000000011e+00, 5.463890000000000136e-01, 1.272434000000000065e+00, 1.115631999999999957e+00, 5.021199999999999969e-02, 0.000000000000000000e+00, 2.016959999999999864e-01, 5.376899999999999735e-02, 2.698400000000000243e-01, 6.949199999999999822e-02, 1.303789999999999949e-01, 7.733130000000000281e-01, 2.080809999999999882e-01, 2.312939999999999996e-01, 1.359652000000000083e+00, 1.874295999999999962e+00, 3.168619999999999770e-01, 4.701400000000000023e-01, 5.441799999999999971e-01, 5.249999999999999806e-02],
[2.199699999999999989e-01, 7.249980000000000313e-01, 1.032342000000000093e+00, 2.437680000000000125e-01, 4.534279999999999977e-01, 2.016959999999999864e-01, 0.000000000000000000e+00, 1.817880000000000051e-01, 5.250960000000000072e-01, 5.405710000000000237e-01, 3.296600000000000086e-01, 4.025777999999999857e+00, 1.141961000000000004e+00, 5.684079999999999799e+00, 3.210671000000000053e+00, 7.434579999999999522e-01, 4.773549999999999738e-01, 1.218270000000000047e-01, 1.281930000000000014e-01, 5.848399999999999821e+00],
[3.616840000000000055e-01, 1.505589999999999984e-01, 1.159680000000000016e-01, 1.117729999999999974e-01, 7.770899999999999475e-01, 5.376899999999999735e-02, 1.817880000000000051e-01, 0.000000000000000000e+00, 2.025619999999999921e-01, 2.335138999999999854e+00, 4.831666000000000238e+00, 4.910030000000000228e-01, 9.858000000000000096e-02, 7.827000000000000624e-02, 2.391949999999999910e-01, 4.051190000000000069e-01, 2.553805999999999798e+00, 9.533943000000000723e+00, 1.345099999999999907e-01, 3.034450000000000203e-01],
[3.694370000000000154e-01, 4.900899999999999701e-02, 2.824659999999999949e-01, 1.731684000000000001e+00, 2.452100000000000113e-02, 2.698400000000000243e-01, 5.250960000000000072e-01, 2.025619999999999921e-01, 0.000000000000000000e+00, 1.464810000000000001e-01, 6.245810000000000528e-01, 2.529516999999999793e+00, 2.163450000000000095e-01, 2.966731999999999925e+00, 6.529255000000000031e+00, 4.744780000000000109e-01, 9.656409999999999716e-01, 1.240659999999999957e-01, 8.913400000000000489e-02, 8.790399999999999603e-02],
[3.100069999999999770e-01, 1.645929999999999893e-01, 6.148599999999999899e-02, 9.748500000000000221e-02, 2.500293999999999794e+00, 6.949199999999999822e-02, 5.405710000000000237e-01, 2.335138999999999854e+00, 1.464810000000000001e-01, 0.000000000000000000e+00, 3.856905999999999946e+00, 1.372889999999999944e-01, 1.060503999999999891e+00, 7.090039999999999676e-01, 3.722610000000000086e-01, 5.925110000000000099e-01, 2.725139999999999785e-01, 1.761438999999999977e+00, 5.303240000000000176e-01, 2.410940000000000027e-01],
[4.693950000000000067e-01, 4.092020000000000102e-01, 1.900010000000000032e-01, 1.750839999999999896e-01, 4.361809999999999854e-01, 1.303789999999999949e-01, 3.296600000000000086e-01, 4.831666000000000238e+00, 6.245810000000000528e-01, 3.856905999999999946e+00, 0.000000000000000000e+00, 3.307200000000000140e-01, 1.642149999999999999e-01, 4.569010000000000016e-01, 4.310450000000000115e-01, 2.855639999999999845e-01, 2.114727999999999941e+00, 3.038533000000000150e+00, 2.013340000000000130e-01, 1.898700000000000110e-01],
[5.579669999999999908e-01, 3.133110000000000062e-01, 5.549529999999999852e+00, 5.781150000000000455e-01, 7.348100000000000465e-02, 7.733130000000000281e-01, 4.025777999999999857e+00, 4.910030000000000228e-01, 2.529516999999999793e+00, 1.372889999999999944e-01, 3.307200000000000140e-01, 0.000000000000000000e+00, 1.218039999999999956e-01, 7.688340000000000174e-01, 4.510950000000000237e-01, 5.057964000000000127e+00, 2.351310999999999929e+00, 1.645250000000000046e-01, 2.769999999999999893e-02, 7.006930000000000103e-01],
[1.959599000000000091e+00, 1.236529999999999990e-01, 1.271639999999999993e-01, 1.919939999999999980e-01, 1.484830000000000039e-01, 2.080809999999999882e-01, 1.141961000000000004e+00, 9.858000000000000096e-02, 2.163450000000000095e-01, 1.060503999999999891e+00, 1.642149999999999999e-01, 1.218039999999999956e-01, 0.000000000000000000e+00, 1.608125999999999944e+00, 7.104890000000000372e-01, 2.788406000000000162e+00, 1.176960999999999924e+00, 2.115609999999999991e-01, 6.996499999999999941e-02, 1.138500000000000068e-01],
[5.567250000000000254e-01, 9.130399999999999627e-02, 5.216460000000000541e-01, 3.417705999999999911e+00, 4.568300000000000138e-02, 2.312939999999999996e-01, 5.684079999999999799e+00, 7.827000000000000624e-02, 2.966731999999999925e+00, 7.090039999999999676e-01, 4.569010000000000016e-01, 7.688340000000000174e-01, 1.608125999999999944e+00, 0.000000000000000000e+00, 3.021994999999999987e+00, 5.488070000000000448e-01, 5.238249999999999851e-01, 1.797709999999999864e-01, 1.722059999999999980e-01, 2.547449999999999992e-01],
[5.316779999999999839e-01, 1.019843000000000055e+00, 1.548990000000000089e-01, 3.184830000000000161e-01, 6.531399999999999706e-02, 1.359652000000000083e+00, 3.210671000000000053e+00, 2.391949999999999910e-01, 6.529255000000000031e+00, 3.722610000000000086e-01, 4.310450000000000115e-01, 4.510950000000000237e-01, 7.104890000000000372e-01, 3.021994999999999987e+00, 0.000000000000000000e+00, 1.001551000000000080e+00, 6.502820000000000267e-01, 1.719950000000000090e-01, 1.257961000000000107e+00, 2.356010000000000049e-01],
[3.887094999999999967e+00, 2.155330999999999886e+00, 5.892680000000000140e-01, 3.124489999999999768e-01, 9.439710000000000045e-01, 1.874295999999999962e+00, 7.434579999999999522e-01, 4.051190000000000069e-01, 4.744780000000000109e-01, 5.925110000000000099e-01, 2.855639999999999845e-01, 5.057964000000000127e+00, 2.788406000000000162e+00, 5.488070000000000448e-01, 1.001551000000000080e+00, 0.000000000000000000e+00, 4.777646999999999977e+00, 4.085320000000000062e-01, 3.109270000000000089e-01, 6.286079999999999446e-01],
[4.582564999999999777e+00, 4.698229999999999906e-01, 4.251590000000000091e-01, 3.315839999999999899e-01, 1.389039999999999997e-01, 3.168619999999999770e-01, 4.773549999999999738e-01, 2.553805999999999798e+00, 9.656409999999999716e-01, 2.725139999999999785e-01, 2.114727999999999941e+00, 2.351310999999999929e+00, 1.176960999999999924e+00, 5.238249999999999851e-01, 6.502820000000000267e-01, 4.777646999999999977e+00, 0.000000000000000000e+00, 1.143979999999999997e+00, 8.055600000000000260e-02, 2.010939999999999950e-01],
[2.924160999999999788e+00, 6.213229999999999587e-01, 3.152610000000000134e-01, 4.652709999999999901e-01, 5.934779999999999500e-01, 4.701400000000000023e-01, 1.218270000000000047e-01, 9.533943000000000723e+00, 1.240659999999999957e-01, 1.761438999999999977e+00, 3.038533000000000150e+00, 1.645250000000000046e-01, 2.115609999999999991e-01, 1.797709999999999864e-01, 1.719950000000000090e-01, 4.085320000000000062e-01, 1.143979999999999997e+00, 0.000000000000000000e+00, 2.396969999999999934e-01, 1.654730000000000090e-01],
[8.432900000000000118e-02, 1.104181000000000079e+00, 5.746600000000000319e-02, 1.143809999999999966e-01, 5.379220000000000113e-01, 5.441799999999999971e-01, 1.281930000000000014e-01, 1.345099999999999907e-01, 8.913400000000000489e-02, 5.303240000000000176e-01, 2.013340000000000130e-01, 2.769999999999999893e-02, 6.996499999999999941e-02, 1.722059999999999980e-01, 1.257961000000000107e+00, 3.109270000000000089e-01, 8.055600000000000260e-02, 2.396969999999999934e-01, 0.000000000000000000e+00, 7.478890000000000260e-01],
[1.394920000000000049e-01, 2.114851999999999954e+00, 4.539520000000000222e-01, 6.345199999999999452e-02, 5.484236000000000111e+00, 5.249999999999999806e-02, 5.848399999999999821e+00, 3.034450000000000203e-01, 8.790399999999999603e-02, 2.410940000000000027e-01, 1.898700000000000110e-01, 7.006930000000000103e-01, 1.138500000000000068e-01, 2.547449999999999992e-01, 2.356010000000000049e-01, 6.286079999999999446e-01, 2.010939999999999950e-01, 1.654730000000000090e-01, 7.478890000000000260e-01, 0.000000000000000000e+00]
])






