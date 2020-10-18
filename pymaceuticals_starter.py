import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st

mouse_metadata_path = "/Users/northwestern/PycharmProjects/MatPlotLibHomework/Mouse_metadata.csv"
study_results_path = "/Users/northwestern/PycharmProjects/MatPlotLibHomework/Study_results.csv"

mouse_metadata = pd.read_csv(mouse_metadata_path)
study_results = pd.read_csv(study_results_path)

combined_study = pd.merge(mouse_metadata, study_results, how="inner", on="Mouse ID")

print(f"Mouse Count: {combined_study['Mouse ID'].count()}")

clean_study = combined_study.drop_duplicates('Mouse ID')

summary = clean_study.groupby('Drug Regimen')['Tumor Volume (mm3)'].describe()
print(summary)

drug_data = pd.DataFrame(combined_study.groupby('Drug Regimen').count())


plt.bar(combined_study['Drug Regimen'].unique(), drug_data['Mouse ID'])

plt.title("Count of Drug Administered")
plt.xticks(rotation='vertical')
plt.show()

sort_by_drugs = combined_study.sort_values(["Drug Regimen"], ascending=True)
capomulin = sort_by_drugs[sort_by_drugs["Drug Regimen"].isin(["Capomulin"])]
ramicane = sort_by_drugs[sort_by_drugs["Drug Regimen"].isin(["Ramicane"])]
infubinol = sort_by_drugs[sort_by_drugs["Drug Regimen"].isin(["Infubinol"])]
ceftamin = sort_by_drugs[sort_by_drugs["Drug Regimen"].isin(["Ceftamin"])]


capomulinQuartile = capomulin['Tumor Volume (mm3)'].quantile([.25,.5,.75])
ramicaneQuartile = ramicane['Tumor Volume (mm3)'].quantile([.25,.5,.75])
infubinolQuartile = infubinol['Tumor Volume (mm3)'].quantile([.25,.5,.75])
ceftaminQuartile = ceftamin['Tumor Volume (mm3)'].quantile([.25,.5,.75])


capomulinIQR = capomulinQuartile[0.75] - capomulinQuartile[0.25]
ramicaneIQR = ramicaneQuartile[0.75] - ramicaneQuartile[0.25]
infubinolIQR = infubinolQuartile[0.75] - infubinolQuartile[0.25]
ceftaminIQR = ceftaminQuartile[0.75] - ceftaminQuartile[0.25]



tumorValue = drug_data['Tumor Volume (mm3)']
top_four_drugs = {'Drug Regimen': ['Capomulin', 'Ramicane', 'Infubinol', 'Ceftamin'],
                  "Tumor Volume (mm3)": [tumorValue['Capomulin'], tumorValue['Ramicane'], tumorValue['Infubinol'], tumorValue['Ceftamin']],
                  "Quartiles": [capomulinQuartile, ramicaneQuartile, infubinolQuartile, ceftaminQuartile],
                  "IQR": [capomulinIQR, ramicaneIQR, infubinolIQR, ceftaminIQR]}


top_four_drugs_frame = pd.DataFrame(top_four_drugs)

print(top_four_drugs_frame)

def showBoxPlot(drug, drugName):
    plt.boxplot(drug['Tumor Volume (mm3)'])
    plt.title(f"Final Tumor Volume ({drugName})")
    plt.ylabel("Tumor Volume (mm3)")
    plt.show()

showBoxPlot(capomulin, "Capomulin")
showBoxPlot(ramicane, "Ramicane")
showBoxPlot(infubinol, "Infubinol")
showBoxPlot(ceftamin, "Ceftamin")
