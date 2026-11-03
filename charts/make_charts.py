import os, openpyxl, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from PIL import Image
v=openpyxl.load_workbook(os.path.join(os.path.dirname(__file__),'..','model','Colgate_Task1_Pro_Forma_Model.xlsx'),data_only=True)
oc=v['Operating Cost Analysis']; P=v['Pro-forma']
hs=[oc[f'{c}4'].value for c in 'BCDEF']; hc=[oc[f'{c}9'].value for c in 'BCDEF']
he=[s-c for s,c in zip(hs,hc)]
fs=[P[f'{c}21'].value for c in 'CDEFG']; fcst=[-P[f'{c}22'].value for c in 'CDEFG']; fe=[P[f'{c}23'].value for c in 'CDEFG']
years=list(range(2018,2028)); sales=hs+fs; ebitda=he+fe; marg=[e/s for e,s in zip(ebitda,sales)]
BLUE,ORANGE,INK,MUTED,GRID='#2a78d6','#eb6834','#0b0b0b','#52514e','#e3e2dd'
names=[f.name for f in font_manager.fontManager.ttflist]
fam='Liberation Serif' if 'Liberation Serif' in names else 'DejaVu Serif'
plt.rcParams.update({'font.family':fam,'font.size':8,'axes.edgecolor':GRID,'axes.labelcolor':MUTED,'xtick.color':MUTED,'ytick.color':MUTED,'text.color':INK})
def clean(ax):
    for s in ('top','right','left'): ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color(MUTED); ax.tick_params(length=0)
    ax.yaxis.grid(True,color=GRID,lw=.8); ax.set_axisbelow(True)
def bars(ax,vals,title,ylab,fmt,lab_idx,ymin=0):
    cols=[BLUE if y<=2022 else ORANGE for y in years]
    ax.bar(years,vals,color=cols,width=.62)
    ax.set_xticks(years); ax.set_xticklabels([str(y)[2:] if False else str(y) for y in years],rotation=0,fontsize=7.5)
    ax.set_ylim(ymin,max(vals)*1.14); clean(ax)
    ax.set_title(title,loc='left',fontsize=10,fontweight='bold',color=INK)
    ax.set_ylabel(ylab,fontsize=8)
    for i in lab_idx: ax.text(years[i],vals[i]+max(vals)*.015,fmt(vals[i]),ha='center',va='bottom',fontsize=8,color=INK)
from matplotlib.patches import Patch
def legend(fig):
    fig.legend(handles=[Patch(color=BLUE,label='Historical (reported)'),Patch(color=ORANGE,label='Forecast (model)')],loc='lower center',ncol=2,frameon=False,fontsize=8.5)
# Figure 1
f1,(a,b)=plt.subplots(1,2,figsize=(7,3.1),dpi=100)
bars(a,sales,'Net sales','$ million',lambda x:f'{x:,.0f}',[0,4,6,9])
bars(b,ebitda,'EBITDA','$ million',lambda x:f'{x:,.0f}',[0,4,6,9])
legend(f1); f1.tight_layout(rect=(0,.08,1,1)); f1.savefig(os.path.join(os.path.dirname(__file__),'Figure1_Net_Sales_and_EBITDA.png'),dpi=300); plt.close(f1)
# Figure 2
f2,(a,b)=plt.subplots(1,2,figsize=(7,3.1),dpi=100)
m=np.array(marg)*100
a.plot(years[:5],m[:5],color=BLUE,lw=2,marker='o',ms=5,mec='#fcfcfb',mew=1.5)
a.plot(years[4:],m[4:],color=ORANGE,lw=2,marker='o',ms=5,mec='#fcfcfb',mew=1.5)
a.set_xticks(years); a.set_xticklabels(years,fontsize=7.5); clean(a); a.set_ylim(20,28)
a.set_title('EBITDA margin',loc='left',fontsize=10,fontweight='bold'); a.set_ylabel('% of sales',fontsize=8)
for i in (0,6,9): a.text(years[i],m[i]+.45,f'{m[i]:.1f}%',ha='center',fontsize=8)
a.annotate(f'{m[4]:.1f}%',(years[4],m[4]),xytext=(-8,-14),textcoords='offset points',ha='center',fontsize=8)
slope,icpt=oc['B14'].value,oc['B13'].value
x=np.array(hs); y=np.array(hc); r2=1-((y-(icpt+slope*x))**2).sum()/((y-y.mean())**2).sum()
xs=np.linspace(15000,21500,50)
b.plot(xs,icpt+slope*xs,color=MUTED,lw=1.5,ls='--',zorder=1)
b.scatter(hs,hc,s=42,color=BLUE,edgecolor='#fcfcfb',linewidth=1.2,zorder=3)
b.scatter(fs,fcst,s=42,color=ORANGE,edgecolor='#fcfcfb',linewidth=1.2,zorder=3)
clean(b); b.xaxis.grid(False)
b.set_title('Operating costs vs sales',loc='left',fontsize=10,fontweight='bold')
b.set_xlabel('Net sales ($ million)',fontsize=8); b.set_ylabel('Costs excl. depreciation ($ million)',fontsize=8)
b.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v,_:f'{v:,.0f}')); b.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v,_:f'{v:,.0f}'))
b.text(.04,.93,f'Costs = {icpt:,.0f} + {slope:.4f} × sales\nR² = {r2:.2f}',transform=b.transAxes,fontsize=8.5,va='top',color=INK)
for yv,xv,yy in zip((2018,2022),(hs[0],hs[4]),(hc[0],hc[4])): b.annotate(str(yv),(xv,yy),xytext=(5,-12),textcoords='offset points',fontsize=8,color=MUTED)
b.annotate('2027',(fs[4],fcst[4]),xytext=(-24,8),textcoords='offset points',fontsize=8,color=MUTED)
legend(f2); f2.tight_layout(rect=(0,.08,1,1)); f2.savefig(os.path.join(os.path.dirname(__file__),'Figure2_EBITDA_Margin_and_Cost_Regression.png'),dpi=300); plt.close(f2)
print('r2',round(r2,4),slope,icpt,[round(x) for x in he],[round(m_,1) for m_ in m])
