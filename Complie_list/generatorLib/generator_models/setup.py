from distutils.core import setup, Extension
import inspect
import glob, sys, os, platform, pickle, gzip

file_list = []

for generator in glob.iglob('./*.c') :
    if platform.system() in ['Linux', 'Darwin'] :
        generator_class_name = generator.split('/')[-1][:-2]
    else :
        generator_class_name = generator.split('\\')[1][:-2]
    file_list.append(generator_class_name)

print (file_list)

# setup(
#         ext_modules = [Extension("_16035d3d071211e36e5cba65d66ee6dca37d7ebbfcf0fe20d909964402653bf1", ["_16035d3d071211e36e5cba65d66ee6dca37d7ebbfcf0fe20d909964402653bf1.c"]),
#             Extension("_2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f", ["_2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.c"]),
#             Extension("_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f", ["_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.c"]),
#             Extension("_6d423e1f15dd9480c4c0e66185d073ba511a802de60979d6a6d9c66f079ee2a7", ["_6d423e1f15dd9480c4c0e66185d073ba511a802de60979d6a6d9c66f079ee2a7.c"]),
#             Extension("_9d836f0eb91c3bf41dab33e6971f76eae91446199aa6508651e6d8ab502df2c4", ["_9d836f0eb91c3bf41dab33e6971f76eae91446199aa6508651e6d8ab502df2c4.c"]),
#             Extension("ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8", ["ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.c"]),
#             Extension("b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81", ["b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81.c"]),
#             Extension("d35f141520a155cbc70cb48892971a1fd6e0470f7e6eecba9792cb9da15bf110", ["d35f141520a155cbc70cb48892971a1fd6e0470f7e6eecba9792cb9da15bf110.c"]),
#             Extension("ef9d0d0c16b2fcf734c4dbeba6625f1f343b6c49a102dd7d4c165a375226a092", ["ef9d0d0c16b2fcf734c4dbeba6625f1f343b6c49a102dd7d4c165a375226a092.c"]),
#             Extension("_1bebca3b5d3a8f929526cf732e8ffd879f12fa84d0597b88b0905649e668578f", ["_1bebca3b5d3a8f929526cf732e8ffd879f12fa84d0597b88b0905649e668578f.c"]), # 1
#             Extension("_2a3744d84c0602c7613a3f25389c302fb48fbdb8469ecfbcf6aebc71a8a41311", ["_2a3744d84c0602c7613a3f25389c302fb48fbdb8469ecfbcf6aebc71a8a41311.c"]), # 2
#             Extension("_3ac1cc89e039aceb4f4dee76edb6400ad698a3cb62bc700d1d24c4e64d5d6b4d", ["_3ac1cc89e039aceb4f4dee76edb6400ad698a3cb62bc700d1d24c4e64d5d6b4d.c"]), # 3
#             Extension("_3bb0af8454ac35e1898db805f9212699beb3255963466a4744fd9c23cf25331a", ["_3bb0af8454ac35e1898db805f9212699beb3255963466a4744fd9c23cf25331a.c"]), # 4
#             Extension("_03dd58d9dd7065a73958a7874256ccb568971e4906b957f58226b62777d7537f", ["_03dd58d9dd7065a73958a7874256ccb568971e4906b957f58226b62777d7537f.c"]), # 5
#             Extension("b39bc4f582cb25442a942f1d0392e419cd38655ee855057293ad8f6d3d27d006", ["b39bc4f582cb25442a942f1d0392e419cd38655ee855057293ad8f6d3d27d006.c"]), # 6
#             Extension("b169b83893e6fcb377ebc4989d80390bf1668232c6f2749c7ab4af4c0703d19d", ["b169b83893e6fcb377ebc4989d80390bf1668232c6f2749c7ab4af4c0703d19d.c"]), # 7
#             Extension("d228727cc591c5a1c73031137d54a2e982c864f4b77ab94ab6834f8ee6788269", ["d228727cc591c5a1c73031137d54a2e982c864f4b77ab94ab6834f8ee6788269.c"]), # 8
#             Extension("Generator", ["Generator.c"])
#             ]
# )
for file in file_list :
    setup(
            ext_modules=[Extension(file, [file+'.c'])]
    )