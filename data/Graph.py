import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 엑셀 파일 불러오기
file_path = 'C:/python/myenv/data_prep_merge.xlsx'
xls = pd.ExcelFile(file_path)

# 첫 번째 시트에서 데이터 불러오기
df = pd.read_excel(xls, sheet_name='Sheet1')

# Extract the relevant columns: YM, TYPE, and RANK_CNT
df_filtered = df[['YM', 'TYPE', 'RANK_CNT']]

# 필터링할 TYPE 값 리스트 (원하는 값으로 수정하세요)
desired_types = ['T4', 'T30', 'T7', 'T8', 'T22']  # 예시로 특정 TYPE 값들만 선택

# 원하는 TYPE 값들만 필터링
df_filtered = df_filtered[df_filtered['TYPE'].isin(desired_types)]

# 데이터를 정렬하고 저장
df_new_filtered_sorted = df_filtered.sort_values(by='YM')

# Convert 'YM' to the desired format 'YYYYMM'
df_new_filtered_sorted['YM'] = pd.to_datetime(df_new_filtered_sorted['YM'], format='%Y%m', errors='coerce').dt.strftime('%Y%m')

# Add a "Season" column to categorize each row based on the YM column
df_new_filtered_sorted['Season'] = pd.cut(pd.to_datetime(df_new_filtered_sorted['YM'], format='%Y%m').dt.month % 12 + 1,
                                          bins=[0, 2, 5, 8, 11],
                                          labels=['Winter', 'Spring', 'Summer', 'Fall'],
                                          include_lowest=True)

# Define a consistent color mapping for each TYPE
color_mapping = {
    'T4': '#FF5733',  # 주황색 예시
    'T30': '#3498DB',  # 파란색 예시
    'T7': '#F39C12',  # 다른 색상 예시
    'T8': '#27AE60',  # 초록색 예시
    'T22': '#2980B9',  # 다른 파란색 예시
}

# Plotting all the data in one plot, separated by hue for TYPE and style for Season
plt.figure(figsize=(18, 10))
sns.barplot(data=df_new_filtered_sorted, x='YM', y='RANK_CNT', hue='TYPE', palette=color_mapping)

# Add titles and labels
plt.title('Combined Graph of All Groups by Type and YM', fontsize=18)
plt.xlabel('YM', fontsize=12)
plt.ylabel('RANK_CNT', fontsize=12)

# Rotate the x-tick labels for better readability
plt.xticks(rotation=45, ha="right", fontsize=10)

# Create a single legend for all subplots (on the right)
plt.legend(title='TYPE', fontsize=12, title_fontsize=14)

# Adjust layout to prevent clipping of tick labels
plt.tight_layout()
plt.show()
