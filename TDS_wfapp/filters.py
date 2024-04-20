from django import template
register = template.Library()

@register.filter
def get_location_count(location_counts, location):
    return location_counts.get(location, 0)

@register.filter
def get_company_size_count(company_size_counts, size):
    return company_size_counts.get(size, 0)

@register.filter
def get_employment_type_count(employment_type_counts, employment_type):
    return employment_type_counts.get(employment_type, 0)