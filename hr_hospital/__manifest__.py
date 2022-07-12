
{
    'name': "Hospital",
    'summary': """
        The module is designed to record doctors and patients.
        Patients are given the opportunity to track their medical history.""",
    'license': 'LGPL-3',
    'author': "Aleksander Gurin",
    'website': "http://www.hr_hospital.com",
    'category': 'Human Resources',
    'version': '15.0.1.0.0',
    'depends': [
        'base'
        ],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_hospital_menus.xml',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/diagnosis_views.xml',
        'views/patient_card_views.xml',
        'views/hr_hospital_views.xml',
    ],
    'support': 'support@hr_hospital.biz',
}
