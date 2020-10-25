# 电视剧信息列表 每条信息包含收视率信息
TV_plays = [('《Give up,hold on to me》', 1.4),
            ('《The private dishes of the husbands》', 1.343),
            ('《My fater-in-low will do martiaiarts》', 0.92),
            ('《Impossible task》', 0.233),
            ('《Sparrow》', 0.411),
            ('《East of dream Avenue》', 0.164),
            ('《Theprodigal son of the new frontier town》', 0.259),
            ('《Distant distance》', 0.394),
            ('《Music legend》', 0.562),
            ]
# 使用内置srted方法进行降序排序
TV_plays = sorted(TV_plays, key=lambda s: s[1], reverse=True)
print('电视剧的收视率排行榜：')
# 循环输出电视剧信息
for TV_plays in TV_plays:
    print(TV_plays[0] + '收视率：' + str(TV_plays[1]) + '%')
