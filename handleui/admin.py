from django.contrib import admin
from handleui.models import ihepip,ihepuser,ihepresults
import os,sys

class MyIPAdmin(admin.ModelAdmin):
    list_display=('ip','chinesename','email','dept')
    search_fields=['ip']
def find_all_ip(search_term):
    ans=[]
    mydir=os.path.join(os.path.dirname(os.path.dirname(__file__)),'results')
    for root,dirs,files in os.walk(mydir):
        for name in files:
            for lines in open(os.path.join(mydir,name)).readlines():
                if lines.upper().find(search_term.upper())!=-1:
                    ans.append(name.split('.html')[0])
                    break
    return ans
class MyResultsAdmin(admin.ModelAdmin):
    list_display=('ip','chinesename','dept','high','mid','low')
    search_fields=('ip',)
    def get_search_results(self, request, queryset, search_term):
        use_distinct=False
        if len(search_term)==0:
            queryset, use_distinct = super(MyResultsAdmin, self).get_search_results(request, queryset, search_term)
        else:
            reload(sys)
            sys.setdefaultencoding('utf-8')
            search_term=unicode(search_term)
            ipset=find_all_ip(search_term)
            queryset=self.model.objects.none()
            for getip in ipset:
                myip=MyIP.objects.filter(ip=getip)
                queryset|=self.model.objects.filter(ip=myip)
        return queryset,use_distinct
class MyUserAdmin(admin.ModelAdmin):
    pass
admin.site.register(ihepip,MyIPAdmin)
admin.site.register(ihepuser,MyUserAdmin)
admin.site.register(ihepresults,MyResultsAdmin)
