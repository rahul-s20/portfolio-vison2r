from models.profiles import Profiles, AboutSelf, Skills, Qualification, Services, Experience
from utils.helper import filter_objects_strict
from flask import jsonify, make_response

allowed_keys = {'first_name', 'middle_name', 'last_name', 'title', 'title_description', 'about_me', 'skill_sets',
                'qualification', 'experience', 'services_offered', 'profile_image', 'github_url', 'linkedin_url',
                'portfolio_web_url', 'contact_no', 'location', 'email'}


def create_profile(body: dict):
    profile_obj = Profiles()
    about_obj = AboutSelf()
    skill_list, qualification_list, experience_list, service_list = [], [], [], []
    try:
        if not body.__contains__('middle_name'):
            body['middle_name'] = ''
        if not body.__contains__('profile_image'):
            body['profile_image'] = ''
        if not body.__contains__('github_url'):
            body['github_url'] = ''
        if not body.__contains__('linkedin_url'):
            body['linkedin_url'] = ''
        if not body.__contains__('portfolio_web_url'):
            body['portfolio_web_url'] = ''
        filtered_data = filter_objects_strict(body, allowed_keys)

        for key, value in filtered_data['about_me'].items():
            setattr(about_obj, key, value)

        for i in filtered_data['skill_sets']:
            skill_obj = Skills()
            for key, value in i.items():
                setattr(skill_obj, key, value)
            skill_list.append(skill_obj)

        for i in filtered_data['qualification']:
            qualification_obj = Qualification()
            for key, value in i.items():
                setattr(qualification_obj, key, value)
            qualification_list.append(qualification_obj)

        for i in filtered_data['experience']:
            experience_obj = Experience()
            for key, value in i.items():
                setattr(experience_obj, key, value)
            experience_list.append(experience_obj)

        for i in filtered_data['services_offered']:
            service_obj = Services()
            for key, value in i.items():
                setattr(service_obj, key, value)
            service_list.append(service_obj)

        for key, value in filtered_data.items():
            if key != 'skill_sets' and key != 'about_me' and key != 'qualification' and key != 'experience' and key != 'services_offered':
                setattr(profile_obj, key, value)

        profile_obj.about_me = about_obj
        profile_obj.skill_sets = skill_list
        profile_obj.qualification = qualification_list
        profile_obj.experience = experience_list
        profile_obj.services_offered = service_list
        profile_obj.save()
        return make_response(jsonify({'success': True, 'data': "Profile created successfully"}), 200)
    except Exception as er:
        raise er
        # return make_response(jsonify({'success': False, 'data': f"Internal server error: {er}"}), 500)


def fetch_own_profile(data: dict):
    available_skills = list()
    all_types = list()
    data_ = {}
    try:
        find_one = Profiles.objects.filter(email=data['email']).first()
        if find_one:
            if len(find_one['skill_sets']) > 0:
                for i in find_one['skill_sets']:
                    if i["type"] not in all_types:
                        all_types.append(i["type"])
                        available_skills.append({
                            "title": i["type"],
                            "details": []
                        })
                for j in find_one['skill_sets']:
                    for k in available_skills:
                        if k["title"] == j["type"]:
                            k["details"].append({"name": j["name"], "weight": j["weight"]})
            data_["skill_sets_mod"] = available_skills
            data_["first_name"] = find_one["first_name"]
            data_["middle_name"] = find_one["middle_name"]
            data_["last_name"] = find_one["last_name"]
            data_["title"] = find_one["title"]
            data_["title_description"] = find_one["title_description"]
            data_["about_me"] = find_one["about_me"]
            data_["skill_sets"] = find_one["skill_sets"]
            data_["qualification"] = find_one["qualification"]
            data_["experience"] = find_one["experience"]
            data_["services_offered"] = find_one["services_offered"]
            data_["profile_image"] = find_one["profile_image"]
            data_["email"] = find_one["email"]
            data_["github_url"] = find_one["github_url"]
            data_["linkedin_url"] = find_one["linkedin_url"]
            data_["portfolio_web_url"] = find_one["portfolio_web_url"]
            data_["contact_no"] = find_one["contact_no"]
            data_["location"] = find_one["location"]
            data_["timestamp"] = find_one["timestamp"]
            data_["last_updated"] = find_one["last_updated"]

        return make_response(jsonify({'success': True, 'data': data_}), 200)
    except Exception as er:
        return make_response(jsonify({'success': False, 'data': f"Internal server error: {er}"}), 500)
