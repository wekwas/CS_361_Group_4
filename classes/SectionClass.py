from SchedulingAPP.models import Section


def get_section_num(section):
    return section.section_num


def set_section_num(section, new_section_num):
    if new_section_num is None:
        raise Exception
    elif not new_section_num.isdigit():
        raise Exception
    elif len(new_section_num) > 3:
        raise Exception
    else:
        section.section_num = new_section_num


def get_ta(section):
    return section.ta


def set_ta(section, new_ta):
    if new_ta is None:
        raise Exception
    elif len(new_ta) > 50:
        raise Exception
    else:
        section.ta = new_ta


def exists(section_num):
    try:
        Section.objects.get(section_num=section_num)
        return True
    except:
        return False


def add_section(section_num, ta):
    if exists(section_num):
        raise Exception("Section already exists")
    else:
        new_section = Section(section_num=" ", ta=" ")
        try:
            set_section_num(new_section, section_num)
            set_ta(new_section, ta)
            new_section.save()
        except:
            return Exception("Incorrect data")


def delete_section(section_num):
    if exists(section_num):
        Section.objects.get(section_num=section_num).delete()
    else:
        raise Exception("Section doesn't exists")
