#match_heatmap.py
#两两文件进行匹配,然后做 heatmap.
#然后遍历所有文件

import os, glob
#print os.__file__
import glbase
#print glbase.__file__
from glbase import *

config.draw_mode = 'pdf'

os.chdir('/Users/wuxiaojian/wujian/4_liujing/6_ATAC_GO_heatmap/2_match_heatmap')

expn = expression(filename='../../0_data/osk_ovsvk_gfp_7f_tpm.csv', format={'force_tsv': False, 'name': 0,}, expn='column[1:]')
#tmp = ['mef', 'D0_7F_Kdm2b', 'D1_7F_Kdm2b', 'D3_7F_Kdm2b', 'D5_7F_Kdm2b', 'D7_7F_Kdm2b', 'esc']
#expn = expn.sliceConditions(tmp)

for f in glob.glob('../1_per_align/GO_*tsv'):
    #print f
    head = os.path.split(f)[1]
    base = head.replace('.tsv', '')
    print base
    arr = genelist(filename=f, format={'force_tsv': True, 'name': 1})
    mapped = arr.map(genelist=expn, key='name')
    mapped_expn = arr.map(genelist=expn, key='name')
    mapped = mapped.removeDuplicates(key='name')
    mapped = mapped.filter_low_expressed(1, 1)
    mapped.saveTSV('%s.tsv' % base)
    #mapped.log(2, 1)
    #bad 
    #mapped.saveTSV('log2_%s.tsv' % base)
    #z_expn = mapped.map(genelist=mapped_expn, key='name')
    #bad 
    #z_expn.saveTSV('%s_z_expn.tsv' % base)
    mapped.convert_to_Z_score()    
    mapped.saveTSV('z_%s.tsv' % base)
    mapped.heatmap(filename='%s.png' % base, colbar_label = 'z_score',  col_font_size = 6, row_font_size = 6, col_cluster = False, row_cluster = True, heat_hei = 0.009 * len(mapped), inshow = False , heat_wid = 0.65, size = (12, 12))
    #bad 

print 'good jobs'





