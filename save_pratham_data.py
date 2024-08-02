import csv

# Data as provided
data = {
    "Introduction": "Pratham is an innovative learning organization created to improve the quality of education in India. As one of the largest non-governmental organizations in the country, Pratham focuses on high-quality, low-cost, and replicable interventions to address gaps in the education system. Established in 1995 to provide education to children in the slums of Mumbai, Pratham has grown both in scope and geographical coverage.",
    "About Us": "Pratham means 'first' in Sanskrit. True to its name, it is the first major organization to achieve lasting, wide-scale success in India's educational landscape. This has been made possible due to various policies and strategies adopted by the organization.",
    "Programs": "Pratham started in Mumbai almost 25 years ago. Then and now, our vision is to ensure that every child is in school and learning well. Then it was Mumbai. Now it is India. In fact, some of Pratham’s key approaches have also spread to Africa. To work towards this goal, Pratham provides a broad-based platform for activities in education and skill development across India. Campaign-Hamara Gaon JOURNEY FROM ‘LEARNING CAMPS-TaRL’ TO HAMARA GAON: Early Childhood Education. Our Early Childhood Education program focuses on the holistic development of children aged 3 to 8 years INTRODUCTION",
    "Job Opportunities": "Manager – Program Management Group. Senior Associate – Program Management, Pratham. Intern – Girls and Women Program. Intern for Maths- Early Years Content.Intern, Content Development and Design – English Program.PILOT, Pratham’s Inspiring Leaders of Tomorrow",
    "Resources": "Resources Media Glimpses Publications. Access to technology is still a questionable reality in most states of India today. The rural teledensity and wireless teledensity figures indicate the economic disparity between rural and urban communities. The onset of the COVID-19 pandemic further brought to light these skewed disparities. In this regard, Pratham explored low-tech resources such as SMS, Radio, TV, and Whatsapp, to ensure that content reached the children and the learning did not halt." ,
    "Contact": "Locate Us Near You Central Offices Delhi Office B- 4/59, Safdarjung Enclave1st Floor, New Delhi - 110 029 Email:info@pratham.org Mumbai Office (Registered) Y.B. Chavan Center, 4th Floor, Gen. J. Bhosale Marg. Nariman Point Mumbai, Maharashtra - 400021 Email:info@pratham.org State Offices Please select a state to know more."
}

# Define CSV file path
csv_file_path = "New_pratham_data.csv"

# Write data to CSV file
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write header (keys of the dictionary)
    writer.writerow(data.keys())
    # Write data (values of the dictionary in a single row)
    writer.writerow(data.values())

print(f"Data has been saved to {csv_file_path}")
