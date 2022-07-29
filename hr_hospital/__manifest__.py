
{
    'name': "Hospital",
    'summary': """
        The module is designed to record doctors and patients.
        Patients are given the opportunity to track their medical history.""",
    'license': 'LGPL-3',
    'author': "Aleksander Gurin",
    'website': "http://www.hr_hospital.com",
    'category': 'Human Resources',
    'version': '15.0.2.0.1',
    'depends': [
        'base'
        ],
    'data': [
        'security/ir.model.access.csv',
        'vizard/adding_doctor_vizard_views.xml',
        'vizard/disease_report_vizard_views.xml',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/diagnosis_views.xml',
        'views/patient_card_views.xml',
        'views/hr_hospital_views.xml',
        'views/contact_person_views.xml',
        'views/disease_views.xml',
        'views/doctor_visit_views.xml',
        'views/personal_doctor_history_view.xml',
        'views/research_views.xml',
        'views/type_of_research_views.xml',
        'views/type_of_sample_views.xml',
        'views/hr_hospital_menus.xml',     
    ],
    'support': 'support@hr_hospital.biz',
}
