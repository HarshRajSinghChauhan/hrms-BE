from rest_framework import serializers
from .models import Attendance
from employees.models import Employee
from employees.serializers import EmployeeSerializer

class AttendanceSerializer(serializers.ModelSerializer):
    employee_id = serializers.CharField(write_only=True)
    employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = Attendance
        fields = ['id', 'employee_id', 'employee', 'date', 'status']

    def create(self, validated_data):
        employee_id = validated_data.pop('employee_id')

        try:
            employee = Employee.objects.get(employee_id=employee_id)
        except Employee.DoesNotExist:
            raise serializers.ValidationError(
                {"employee_id": "Employee with this ID does not exist."}
            )

        return Attendance.objects.create(
            employee=employee,
            **validated_data
        )