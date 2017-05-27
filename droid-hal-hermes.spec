# These and other macros are documented in dhd/droid-hal-device.inc
%define device hermes
%define vendor xiaomi
%define vendor_pretty Xiaomi
%define device_pretty Redmi Note 2
%define installable_zip 1
%define droid_target_armv7hl 1
%define straggler_files \
/bugreports \
/d \
/file_contexts.bin \
/property_contexts \
/sdcard \
/selinux_version \
/service_contexts \
/vendor \
%{nil}
%define makefstab_skip_entries /tmp
%include rpm/dhd/droid-hal-device.inc
