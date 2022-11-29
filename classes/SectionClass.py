from SchedulingAPP.models import Section


class SectionClass:
    def __init__(self):
        self.section = Section(section_num=" ", ta=" ")

    def get_section_num(self):
        return self.section.section_num

    def set_section_num(self, new_section_num):
        if new_section_num is None:
            raise Exception
        elif not new_section_num.isdigit():
            raise Exception
        elif len(new_section_num) > 3:
            raise Exception
        else:
            self.section.section_num = new_section_num

    def get_ta(self):
        return self.section.ta

    def set_ta(self, new_ta):
        if new_ta is None:
            raise Exception
        elif len(new_ta) > 50:
            raise Exception
        else:
            self.section.ta = new_ta

    def add_section(self):
        try:
            Section.objects.get(section_num=self.section.section_num)
        except:
            self.section.save()
            return
        raise Exception

    def delete_section(self):
        self.section.delete()
