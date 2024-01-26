import seaborn as sns
import matplotlib.pyplot as plt

def calculate_percentage(df, group_columns):
    """グループ化し、各グループ内での割合を計算する"""
    grouped_df = df.groupby(group_columns).size().reset_index(name='counts')
    grouped_df['percentage'] = grouped_df.groupby(group_columns[0])['counts'].transform(lambda x: x / x.sum() * 100)
    return grouped_df

def select_top5(grouped_df, group_column):
    """各グループで割合が最も高い上位5つを選択する"""
    return grouped_df.groupby(group_column).apply(lambda x: x.nlargest(5, 'percentage')).reset_index(drop=True)

def plot_percentage(top5_df, x_column, hue_column, title):
    """割合を棒グラフで表示する"""
    plt.figure(figsize=(10, 6))
    sns.barplot(x=x_column, y='percentage', hue=hue_column, data=top5_df)
    plt.title(title)
    plt.show()

# 年齢と犬種でグループ化し、各年齢グループ内での犬種の割合を計算
grouped_age = calculate_percentage(df, ['ALTER', 'RASSE'])

# 各年齢グループで割合が最も高い上位5つの犬種を選択
top5_age = select_top5(grouped_age, 'ALTER')

# 年齢ごとの犬種の割合を棒グラフで表示
plot_percentage(top5_age, 'ALTER', 'RASSE', 'Top 5 Percentage of Dog Breeds by Age')

# 性別と犬種でグループ化し、各性別グループ内での犬種の割合を計算
grouped_gender = calculate_percentage(df, ['GESCHLECHT', 'RASSE'])

# 各性別グループで割合が最も高い上位5つの犬種を選択
top5_gender = select_top5(grouped_gender, 'GESCHLECHT')

# 性別ごとの犬種の割合を棒グラフで表示
plot_percentage(top5_gender, 'GESCHLECHT', 'RASSE', 'Top 5 Percentage of Dog Breeds by Gender')