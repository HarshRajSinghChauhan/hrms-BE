from rest_framework import serializers
from .models import Employee, Attendance


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    employee_id = serializers.CharField(write_only=True, required=False)
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

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance