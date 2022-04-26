CC = /opt/hipSYCL/bin/syclcc-clang --hipsycl-targets="hip:gfx900" -fPIC # -frtti

default: libexamples.a

libexamples.a: examples.o
	ar rcs $@ $^
    
examples.o: examples.c examples.h
#	$(CC) -L/usr/local/cuda/lib64 -lcudart -lrt -lstdc++ -c $<
	$(CC) -c $<
#	$(CC) -static -L/opt/hipSYCL/lib/hipSYCL -lrt-backend-cuda -L/opt/hipSYCL/lib -lhipSYCL-rt -c $<

clean:
	rm *.o *.a
