from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from myapp.models import Train

# แสดงข้อมูลทั้งหมด
def index(request):
    all_train = Train.objects.all()
    return render(request, "index.html", {"all_train": all_train})

# ฟังก์ชั่นแก้ไขข้อมูล
def edit(request, id):
    # ค้นหาข้อมูล Train ที่มี id ตรงกัน
    train = get_object_or_404(Train, id=id)
    
    if request.method == 'POST':
        # รับข้อมูลจากฟอร์มและอัปเดตข้อมูล
        train.name = request.POST.get("name")
        train.last = request.POST.get("last")
        train.job = request.POST.get("job")
        train.section = request.POST.get("section")
        train.email = request.POST.get("email")
        train.phone = request.POST.get("phone")
        
        # บันทึกข้อมูลที่อัปเดต
        train.save()
        
        # หลังจากบันทึกแล้ว เปลี่ยนไปหน้าแรก
        return redirect('/')
    
    # ถ้าเป็น GET หรือฟอร์มแรกแสดง
    return render(request, "edit.html", {"train": train})

# ฟอร์มสำหรับกรอกข้อมูล
def form(request):
    if request.method == "POST":
        # รับข้อมูลจากฟอร์ม
        name = request.POST.get("name")
        last = request.POST.get("last")
        job = request.POST.get("job")
        section = request.POST.get("section")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        # บันทึกข้อมูลในฐานข้อมูล
        train = Train.objects.create(
            name=name,
            last=last,
            job=job,
            section=section,
            email=email,
            phone=phone
        )

        # หลังจากบันทึกแล้ว เปลี่ยนไปหน้าแรก
        return redirect("/")
    else:
        # แสดงฟอร์ม
        return render(request, "form.html")

def search(request):
    search_query = request.GET.get('search', '')  # รับค่าจากฟอร์มการค้นหาหรือ query string
    results = Train.objects.all()  # ดึงข้อมูลทั้งหมด

    # ถ้ามีการค้นหา
    if search_query:
        results = results.filter(name__icontains=search_query)  # ค้นหาจากชื่อที่ตรงกับคำค้นหาหรือไม่
    return render(request, "search.html", {"all_train": results, "search_query": search_query})

    if search_query:
        # ค้นหาข้อมูลจากฐานข้อมูล
        results = Train.objects.filter(name__icontains=search_query)  # ค้นหาข้อมูลที่ชื่อมีคำค้นหานี้

    return render(request, 'search.html', {'results': results, 'search_query': search_query})

    # ฟังก์ชั่นลบข้อมูล
def delete(request, id):
    # ค้นหาข้อมูล Train ที่มี id ตรงกัน
    train = get_object_or_404(Train, id=id)
    
    # ลบข้อมูลที่ค้นพบ
    train.delete()
    
    # หลังจากลบแล้วให้กลับไปที่หน้าแรก
    return redirect('/')