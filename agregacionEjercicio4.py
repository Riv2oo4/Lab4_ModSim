def group_attack_rates(df, by):
    agg = df.groupby(by).agg(pop=('infected','size'),
                             cases=('infected','sum'))
    agg['attack_rate'] = agg['cases'] / agg['pop']
    return agg

rates_age = group_attack_rates(df, 'age')
rates_vax = group_attack_rates(df, 'vaccinated')
RR_vax = (rates_vax.loc[False,'attack_rate'] /
          rates_vax.loc[True,'attack_rate'])
