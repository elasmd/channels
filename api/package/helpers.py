from api.program.models import Program


def packageinfo(item):
    return {
                'name': item.name,
                'price': item.price,
                'programs':[
                    item.name for item in Program.objects.filter(package=item)
                ]
            }