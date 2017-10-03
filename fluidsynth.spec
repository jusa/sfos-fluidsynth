Name:       fluidsynth
Summary:    A SoundFont Synthesizer
Version:    1.1.6
Release:    1
Group:      Applications/Multimedia
License:    LGPL 2.0
URL:        http://www.fluidsynth.org/
Source:     %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(libpulse-simple)

%description
FluidSynth is a real-time software synthesizer based on the SoundFont 2 specifications and has reached widespread distribution. FluidSynth itself does not have a graphical user interface, but due to its powerful API several applications utilize it and it has even found its way onto embedded systems and is used in some mobile apps.

%package -n libfluidsynth-devel
Summary:    Fluidsynth development headers and libraries
Group:      Development/Libraries
Requires:   libfluidsynth = %{version}-%{release}

%description -n libfluidsynth-devel
Development files for fluidsynth.

%package -n libfluidsynth
Summary:    Fluidsynth libraries
Group:      System/Libraries

%description -n libfluidsynth
FluidSynth is a real-time software synthesizer based on the SoundFont 2 specifications and has reached widespread distribution. FluidSynth itself does not have a graphical user interface, but due to its powerful API several applications utilize it and it has even found its way onto embedded systems and is used in some mobile apps.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
make %{?jobs:-j%jobs}

%post -n libfluidsynth -p /sbin/ldconfig

%postun -n libfluidsynth -p /sbin/ldconfig

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%{_bindir}/fluidsynth

%files -n libfluidsynth
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libfluidsynth.so.1.5.2
%{_libdir}/libfluidsynth.so.1

%files -n libfluidsynth-devel
%defattr(-,root,root,-)
%{_libdir}/libfluidsynth.so
%{_libdir}/pkgconfig/fluidsynth.pc
%{_datadir}/man/man1/fluidsynth.1.gz
%dir %{_includedir}/fluidsynth
%{_includedir}/fluidsynth/settings.h
%{_includedir}/fluidsynth/mod.h
%{_includedir}/fluidsynth/midi.h
%{_includedir}/fluidsynth/ramsfont.h
%{_includedir}/fluidsynth/gen.h
%{_includedir}/fluidsynth/audio.h
%{_includedir}/fluidsynth/sfont.h
%{_includedir}/fluidsynth/seq.h
%{_includedir}/fluidsynth/synth.h
%{_includedir}/fluidsynth/seqbind.h
%{_includedir}/fluidsynth/version.h
%{_includedir}/fluidsynth/log.h
%{_includedir}/fluidsynth/voice.h
%{_includedir}/fluidsynth/event.h
%{_includedir}/fluidsynth/shell.h
%{_includedir}/fluidsynth/misc.h
%{_includedir}/fluidsynth/types.h
%{_includedir}/fluidsynth.h
